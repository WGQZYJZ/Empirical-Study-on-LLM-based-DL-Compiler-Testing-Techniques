import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg



class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.dropout_fc = torch.nn.Dropout(0.1)

    def forward(self, x1, x2):
        v1 = self.dropout_fc(x2)
        v2 = self.dropout_fc(x1)
        v3 = torch.matmul(v1, v2.transpose((- 2), (- 1)))
        v4 = v3.mul(0.5)
        v5 = torch.nn.functional.softmax(v4, dim=(- 1))
        v6 = torch.nn.functional.dropout(v5, p=0.1)
        v7 = torch.matmul(v6, x2)
        return v7



func = Model().to('cuda')



x1 = torch.randn(1, 23)



x2 = torch.randn(3, 50)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x50 and 23x1)

jit:
Failed running call_function <built-in method matmul of type object at 0x71740a2699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 50)), FakeTensor(..., device='cuda:0', size=(23, 1))), **{}):
a and b must have same reduction dim, but got [3, 50] X [23, 1].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
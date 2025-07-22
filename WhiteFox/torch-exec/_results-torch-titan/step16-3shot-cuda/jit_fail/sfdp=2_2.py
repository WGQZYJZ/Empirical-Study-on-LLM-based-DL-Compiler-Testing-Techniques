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
        self.dropout = torch.nn.Dropout(0.1)

    def forward(self, x1, x2, x3, x4):
        v1 = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        v2 = v1.div(0.1)
        v3 = torch.nn.functional.softmax(v2, dim=(- 1))
        v4 = self.dropout(v3)
        v5 = v4.matmul(x3)
        return v5



func = Model().to('cuda')



x1 = torch.randn(3, 10)



x2 = torch.randn(3, 20)



x3 = torch.randn(3, 20)



x4 = torch.randn(3, 30)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x10 and 20x3)

jit:
Failed running call_function <built-in method matmul of type object at 0x79e386a699e0>(*(FakeTensor(..., device='cuda:0', size=(3, 10)), FakeTensor(..., device='cuda:0', size=(20, 3))), **{}):
a and b must have same reduction dim, but got [3, 10] X [20, 3].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
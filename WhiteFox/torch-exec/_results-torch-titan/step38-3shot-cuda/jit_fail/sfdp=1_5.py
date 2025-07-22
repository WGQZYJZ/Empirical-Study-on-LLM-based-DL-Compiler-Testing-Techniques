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
        self.linear = torch.nn.Linear(64, 15)

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, self.linear.weight)
        v2 = v1.softmax((- 1))
        v3 = torch.nn.functional.dropout(v2, p=0.2)
        v4 = v3.matmul(x2)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 32, 64)



x2 = torch.randn(1, 21, 15)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (32x64 and 15x64)

jit:
Failed running call_function <built-in method matmul of type object at 0x7b533d6699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 32, 64)), Parameter(FakeTensor(..., device='cuda:0', size=(15, 64), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [32, 64] X [15, 64].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
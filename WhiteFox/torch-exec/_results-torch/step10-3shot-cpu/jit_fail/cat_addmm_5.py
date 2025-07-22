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

    def forward(self, x1, x2, b1, b2):
        v1 = torch.addmm(x1, b1, x2)
        v2 = torch.cat([v1], dim=b2.dim() - 1)
        return v2


func = Model().to('cpu')


x1 = torch.randn(1, 256, 1024)

x2 = torch.randn(1, 12, 256, 1024)

b1 = torch.randn(1, 256, 12)
b2 = 1

test_inputs = [x1, x2, b1, b2]

# JIT_FAIL
'''
direct:
mat1 must be a matrix, got 3-D tensor

jit:
Failed running call_function <built-in method addmm of type object at 0x71ddb4396ec0>(*(FakeTensor(..., size=(1, s3, s4)), FakeTensor(..., size=(1, 256, 12)), FakeTensor(..., size=(1, s0, s1, s2))), **{}):
a must be 2D

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
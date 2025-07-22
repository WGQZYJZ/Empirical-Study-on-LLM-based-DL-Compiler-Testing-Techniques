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

    def forward(self, x, y):
        v1 = torch.mm(x, y)
        v2 = torch.mm(x, y)
        v3 = torch.mm(x, y)
        v4 = torch.mm(x, y)
        v5 = torch.mm(x, y)
        v6 = torch.mm(x, y)
        v7 = torch.mm(x, y)
        v8 = torch.mm(x, y)
        return torch.cat([v1, v2, v3, v4, v5, v6, v7, v8], 1)



func = Model().to('cpu')


x = torch.randn(2, 4)

y = torch.randn(3, 4)

test_inputs = [x, y]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x4 and 3x4)

jit:
Failed running call_function <built-in method mm of type object at 0x720785196ec0>(*(FakeTensor(..., size=(2, s2)), FakeTensor(..., size=(s0, s1))), **{}):
a and b must have same reduction dim, but got [2, s2] X [s0, s1].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
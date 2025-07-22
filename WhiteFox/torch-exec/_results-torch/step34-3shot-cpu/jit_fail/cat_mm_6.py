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

    def forward(self, x1, x2, x3, x4, x5):
        v = torch.cat([torch.mm(x1, x2), torch.mm(x3, x4), torch.mm(x5, x1), torch.mm(x1, x2)], 1)
        return torch.cat([v, v], 1)



func = Model().to('cpu')


x1 = torch.randn(4, 2)

x2 = torch.randn(2, 4)

x3 = torch.randn(2, 2)

x4 = torch.randn(2, 4)

x5 = torch.randn(2, 2)

test_inputs = [x1, x2, x3, x4, x5]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x2 and 4x2)

jit:
Failed running call_function <built-in method mm of type object at 0x700da2b96ec0>(*(FakeTensor(..., size=(2, 2)), FakeTensor(..., size=(s2, s0))), **{}):
a and b must have same reduction dim, but got [2, 2] X [s2, s0].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
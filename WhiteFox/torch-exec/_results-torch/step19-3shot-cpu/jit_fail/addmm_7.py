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

    def forward(self, x1, x2, inp):
        t1 = torch.mm(inp, inp)
        v1 = t1 + x1
        v2 = torch.mm(v1, x2)
        return v2



func = Model().to('cpu')


inp = torch.randn(4, 3)

x1 = torch.randn(3, 3)

x2 = torch.randn(3, 2)

test_inputs = [inp, x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x2 and 3x2)

jit:
Failed running call_function <built-in method mm of type object at 0x7f6611d96ec0>(*(FakeTensor(..., size=(s0, s1)), FakeTensor(..., size=(s0, s1))), **{}):
a and b must have same reduction dim, but got [s0, s1] X [s0, s1].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
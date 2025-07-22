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

    def forward(self, x1, x2, inp1, inp2, inp3):
        v1 = torch.mm(x1.transpose(0, 1), inp1)
        v2 = torch.mm(x1, v1) + torch.mm(x2, inp2)
        v3 = v2 + inp3
        return v3



func = Model().to('cpu')


x1 = torch.randn(1024, 1321)

x2 = torch.randn(1024, 1)

inp1 = torch.randn(1321, 1)

inp2 = torch.randn(1, 1)

inp3 = torch.randn(1, 376)

test_inputs = [x1, x2, inp1, inp2, inp3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1321x1024 and 1321x1)

jit:
Failed running call_function <built-in method mm of type object at 0x76dae6d96ec0>(*(FakeTensor(..., size=(s1, s0)), FakeTensor(..., size=(s2, 1))), **{}):
a and b must have same reduction dim, but got [s1, s0] X [s2, 1].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
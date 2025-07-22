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

    def forward(self, x1, x2, inp1, inp2):
        v1 = torch.mm(x1, inp1) + torch.mm(x2, inp1)
        v2 = v1 + inp2
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 1)

x2 = torch.randn(2, 2)

inp1 = torch.randn(1, 3)

inp2 = torch.randn(3, 3)

test_inputs = [x1, x2, inp1, inp2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x2 and 1x3)

jit:
Failed running call_function <built-in method mm of type object at 0x76dae6d96ec0>(*(FakeTensor(..., size=(s0, s1)), FakeTensor(..., size=(1, 3))), **{}):
a and b must have same reduction dim, but got [s0, s1] X [1, 3].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
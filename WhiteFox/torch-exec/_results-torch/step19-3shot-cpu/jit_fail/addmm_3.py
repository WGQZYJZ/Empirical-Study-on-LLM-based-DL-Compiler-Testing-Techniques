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

    def forward(self, x1, x2, x3, inp):
        v1 = torch.mm(x1, x2)
        v2 = v1.mm(x3)
        return v1.mm(inp + v2) + torch.mm(x1, inp)



func = Model().to('cpu')


x1 = torch.randn(2, 2)

x2 = torch.randn(2, 1)

x3 = torch.randn(1, 3)

inp = torch.randn(2, 3)

test_inputs = [x1, x2, x3, inp]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x1 and 2x3)

jit:
Failed running call_method mm(*(FakeTensor(..., size=(s1, 1)), FakeTensor(..., size=(s1, 3))), **{}):
a and b must have same reduction dim, but got [s1, 1] X [s1, 3].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
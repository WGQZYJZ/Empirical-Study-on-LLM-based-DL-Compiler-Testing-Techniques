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
        with torch.no_grad():
            v1 = torch.mm(x1, x2)
            return v1 + inp



func = Model().to('cpu')


x1 = torch.randn(3, 3)

x2 = torch.randn(1, 3)

inp = torch.randn(3, 3)

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x3 and 1x3)

jit:
Failed running call_function <built-in method mm of type object at 0x766cd0996ec0>(*(FakeTensor(..., size=(3, 3)), FakeTensor(..., size=(1, 3))), **{}):
a and b must have same reduction dim, but got [3, 3] X [1, 3].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
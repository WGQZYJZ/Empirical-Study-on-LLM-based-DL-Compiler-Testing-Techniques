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
        v1 = torch.mm(inp1, inp2)
        v2 = torch.mm(x1, x2) + v1
        return v2



func = Model().to('cpu')


x1 = torch.randn(3, 3)

x2 = torch.randn(555, 3)

inp1 = torch.randn(6, 6)

inp2 = torch.randn(6, 6)

test_inputs = [x1, x2, inp1, inp2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (3x3 and 555x3)

jit:
Failed running call_function <built-in method mm of type object at 0x77317d596ec0>(*(FakeTensor(..., size=(s6, s7)), FakeTensor(..., size=(s4, s5))), **{}):
a and b must have same reduction dim, but got [s6, s7] X [s4, s5].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
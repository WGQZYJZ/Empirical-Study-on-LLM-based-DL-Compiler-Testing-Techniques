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

    def forward(self, x1, x2):
        v1 = torch.cat([torch.mm(x1, x2), torch.mm(x1, x2)], 1)
        return torch.cat([torch.mm(v1, torch.rand(1, 1)), torch.mm(x1, torch.cat([x1, x2], 1)), torch.mm(v1, torch.rand(1, 1)), torch.mm(x1, torch.cat([x2, x2], 1)), torch.mm(v1, torch.rand(1, 1), 1), torch.mm(x1, torch.cat([x2, x2], 1))], 1)



func = Model().to('cpu')


x1 = torch.randn(2, 1)

x2 = torch.randn(1, 2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (2x4 and 1x1)

jit:
Failed running call_function <built-in method mm of type object at 0x7b4361396ec0>(*(FakeTensor(..., size=(s1, 2*s0)), FakeTensor(..., size=(1, 1))), **{}):
a and b must have same reduction dim, but got [s1, 2*s0] X [1, 1].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
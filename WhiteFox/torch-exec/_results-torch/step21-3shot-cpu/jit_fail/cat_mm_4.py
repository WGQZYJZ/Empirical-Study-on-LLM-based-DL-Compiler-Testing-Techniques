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
        v1 = torch.mm(x1, x2)
        v1 = torch.mm(x1, x2)
        v1 = torch.mm(v1, x2)
        v2 = torch.mm(x1, x2)
        v2 = torch.mm(v2, x2)
        v2 = torch.mm(v2, x2)
        v3 = torch.mm(x1, x2)
        v3 = torch.mm(v3, x2)
        v4 = torch.mm(x1, x2)
        v4 = torch.mm(v4, x2)
        return torch.cat([v1, v2, v3, v4], 1)



func = Model().to('cpu')


x1 = torch.randn(1, 10)

x2 = torch.randn(10, 1)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x1 and 10x1)

jit:
Failed running call_function <built-in method mm of type object at 0x7a2290596ec0>(*(FakeTensor(..., size=(1, 1)), FakeTensor(..., size=(s0, 1))), **{}):
a and b must have same reduction dim, but got [1, 1] X [s0, 1].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x3)
        v2 = torch.mm(x2, x4)
        v3 = v1 + v2
        return v3



func = Model().to('cpu')


x1 = torch.randn(5, 3)

x2 = torch.randn(3, 5)

x3 = torch.randn(5, 3)

x4 = torch.randn(3, 5)

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (5x3 and 5x3)

jit:
Failed running call_function <built-in method mm of type object at 0x7f3e80996ec0>(*(FakeTensor(..., size=(5, 3)), FakeTensor(..., size=(5, 3))), **{}):
a and b must have same reduction dim, but got [5, 3] X [5, 3].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def forward(self, x, x1, x2, d=1):
        x3 = x1 * x2
        x4 = torch.mm(x, x)
        x5 = x * x
        x6 = x4 - x5
        x7 = torch.mm(x5, x6)
        x8 = torch.mm(x2, x5)
        x9 = x5 ** d
        x10 = x4 * x3
        x11 = x1 - x2
        x12 = torch.mm(x11, x1)
        x13 = torch.mm(x6, x7)
        return x10 - x12 + x13 - x8 - x9 + x9



func = Model().to('cpu')


x1 = torch.randn(12, 10)

x2 = torch.randn(12, 10)

x = torch.randn(10, 10)

test_inputs = [x1, x2, x]

# JIT_FAIL
'''
direct:
The size of tensor a (12) must match the size of tensor b (10) at non-singleton dimension 0

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(s0, s1)), FakeTensor(..., size=(s2, s1))), **{}):
The size of tensor a (s0) must match the size of tensor b (s2) at non-singleton dimension 0)

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
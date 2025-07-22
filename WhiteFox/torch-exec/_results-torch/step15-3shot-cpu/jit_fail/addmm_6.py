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
        v1 = torch.mm(inp, x2)
        v2 = v1 + x1
        return v2.T



func = Model().to('cpu')


x1 = torch.randn(100, 100)

x2 = torch.randn(0, 0)

inp = torch.randn(100, 0)

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
The size of tensor a (0) must match the size of tensor b (100) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(s0, 0)), FakeTensor(..., size=(s1, s2))), **{}):
The size of tensor a (0) must match the size of tensor b (s2) at non-singleton dimension 1)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
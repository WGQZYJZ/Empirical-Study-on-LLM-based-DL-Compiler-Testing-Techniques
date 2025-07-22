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
        v1 = torch.mm(x1.T, inp.T)
        v2 = v1 + x2
        return v2



func = Model().to('cpu')


x1 = torch.randn(2, 222)

x2 = torch.randn(2, 2)

inp = torch.randn(222, 2)

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
The size of tensor a (222) must match the size of tensor b (2) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(s1, s2)), FakeTensor(..., size=(s4, s5))), **{}):
The size of tensor a (s2) must match the size of tensor b (s5) at non-singleton dimension 1)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
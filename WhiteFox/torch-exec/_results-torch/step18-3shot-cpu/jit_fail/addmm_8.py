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
        v1 = x1 + x2
        v2 = torch.mm(v1, inp)
        return v2



func = Model().to('cpu')


x1 = torch.randn(3, 5, 6, 12)

x2 = torch.randn(3, 5, 6, 6)

inp = torch.randn(6, 12)

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
The size of tensor a (12) must match the size of tensor b (6) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(s0, s1, s2, s3)), FakeTensor(..., size=(s4, s5, s6, s7))), **{}):
The size of tensor a (s3) must match the size of tensor b (s7) at non-singleton dimension 3)

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        v1 = torch.mm(x1, x2)
        v2 = inp + v1
        v3 = v2 + inp
        return v3



func = Model().to('cpu')


x1 = torch.randn(5, 5)

x2 = torch.randn(5, 5)

inp = torch.randn(3, 3, 3)

test_inputs = [x1, x2, inp]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (5) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(3, 3, s1)), FakeTensor(..., size=(s0, 5))), **{}):
The size of tensor a (s1) must match the size of tensor b (5) at non-singleton dimension 2)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
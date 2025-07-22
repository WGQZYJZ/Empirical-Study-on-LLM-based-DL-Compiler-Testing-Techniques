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

    def forward(self, x):
        y = torch.cat([x, x, x], dim=-1)
        x = x.tanh()
        x = y * x
        return x



func = Model().to('cpu')


x = torch.randn(2, 3, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (12) must match the size of tensor b (4) at non-singleton dimension 2

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(s0, s1, 3*s2)), FakeTensor(..., size=(s0, s1, s2))), **{}):
The size of tensor a (3*s2) must match the size of tensor b (s2) at non-singleton dimension 2)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
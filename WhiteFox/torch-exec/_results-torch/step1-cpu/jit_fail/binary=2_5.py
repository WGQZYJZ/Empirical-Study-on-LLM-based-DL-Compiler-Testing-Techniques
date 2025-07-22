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
        self.conv = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)

    def forward(self, x, other):
        v1 = self.conv(x)
        v2 = other
        v3 = v2 - v1
        return v3


func = Model().to('cpu')


x = torch.randn(1, 3, 64, 64)

other = torch.randn(1, 3, 64, 64)

test_inputs = [x, other]

# JIT_FAIL
'''
direct:
The size of tensor a (3) must match the size of tensor b (8) at non-singleton dimension 1

jit:
Failed running call_function <built-in function sub>(*(FakeTensor(..., size=(1, s0, 64, 64)), FakeTensor(..., size=(1, 8, 64, 64))), **{}):
The size of tensor a (s0) must match the size of tensor b (8) at non-singleton dimension 1)

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
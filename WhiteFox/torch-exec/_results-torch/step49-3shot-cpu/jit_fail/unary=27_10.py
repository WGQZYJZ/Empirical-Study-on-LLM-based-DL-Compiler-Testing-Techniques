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

    def __init__(self, min, max):
        super().__init__()
        self.avgpool = torch.nn.AvgPool2d(3, stride=1, padding=1)
        self.linear = torch.nn.Linear(10, 16)
        self.min = min
        self.max = max

    def forward(self, x1, x2, x3):
        v1 = self.avgpool(x1)
        v2 = self.linear(x2)
        v3 = torch.max(v1, v2)
        v4 = torch.clamp_min(v3, self.min)
        v5 = torch.clamp_max(v4, self.max)
        return (v5, v2, x3)


min = -6
max = 7.2

func = Model(min, max).to('cpu')


x1 = torch.randn(1, 16, 100, 100)

x2 = torch.randn(1, 10)

x3 = torch.randn(1, 3, 32, 32)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (100) must match the size of tensor b (16) at non-singleton dimension 3

jit:
Failed running call_function <built-in method max of type object at 0x7aea1a596ec0>(*(FakeTensor(..., size=(1, 16, 100, 100)), FakeTensor(..., size=(1, 16))), **{}):
Attempting to broadcast a dimension of length 16 at -1! Mismatching argument at index 1 had torch.Size([1, 16]); but expected shape should be broadcastable to [1, 16, 100, 100]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
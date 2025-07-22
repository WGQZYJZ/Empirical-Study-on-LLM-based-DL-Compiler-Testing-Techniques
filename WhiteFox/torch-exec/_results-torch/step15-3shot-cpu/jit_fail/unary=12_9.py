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
        self.conv1 = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 32, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(32, 32, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = F.hardtanh(v1)
        v3 = torch.mul(v1, v2)
        v4 = self.conv2(v3)
        v5 = F.hardtanh(v4)
        v6 = torch.mul(v4, v5)
        v7 = v5 * v6
        v8 = self.conv3(v7)
        v9 = torch.mul(v8, v7)
        return v9



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (70) must match the size of tensor b (68) at non-singleton dimension 3

jit:
Failed running call_function <built-in method mul of type object at 0x7dd621996ec0>(*(FakeTensor(..., size=(1, 32, s0 + 6, s1 + 6)), FakeTensor(..., size=(1, 32, s0 + 4, s1 + 4))), **{}):
The size of tensor a (s1 + 6) must match the size of tensor b (s1 + 4) at non-singleton dimension 3)

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
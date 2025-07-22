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
        self.conv1 = torch.nn.Conv2d(3, 32, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(32, 64, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = 3 + x1
        v2 = self.conv1(v1)
        t1 = self.conv2(v2)
        v3 = 3 + t1
        v4 = torch.clamp_min(v3, 0)
        v5 = torch.clamp_max(v4, 6)
        v6 = v2 * v5
        v7 = v6 / 6
        v8 = v1 * v7
        v9 = v8 / 6
        return v9



func = Model().to('cpu')


x1 = torch.randn(2, 3, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (64) at non-singleton dimension 1

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., size=(s0, 32, s1, s2)), FakeTensor(..., size=(s0, 64, s1, s2))), **{}):
The size of tensor a (32) must match the size of tensor b (64) at non-singleton dimension 1)

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
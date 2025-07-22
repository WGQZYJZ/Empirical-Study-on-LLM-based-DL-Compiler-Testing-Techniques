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
        self.pool = torch.nn.AvgPool2d(2, stride=2, padding=1, ceil_mode=True)
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, x1, x2, x3):
        v1 = self.pool(x1)
        v2 = self.conv1(x1)
        v3 = v1 + v2
        v4 = torch.relu(v3)
        v5 = self.conv2(v4)
        v6 = v1 + v5
        v7 = torch.relu(v6)
        v8 = self.conv3(v7)
        v9 = v1 + v8
        v10 = torch.relu(v9)
        return v10



func = Model().to('cpu')


x1 = torch.randn(16, 16, 64, 64)

x2 = torch.randn(16, 16, 64, 64)

x3 = torch.randn(16, 16, 64, 64)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (33) must match the size of tensor b (64) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(16, 16, 33, 33)), FakeTensor(..., size=(16, 16, 64, 64))), **{}):
Attempting to broadcast a dimension of length 64 at -1! Mismatching argument at index 1 had torch.Size([16, 16, 64, 64]); but expected shape should be broadcastable to [16, 16, 33, 33]

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
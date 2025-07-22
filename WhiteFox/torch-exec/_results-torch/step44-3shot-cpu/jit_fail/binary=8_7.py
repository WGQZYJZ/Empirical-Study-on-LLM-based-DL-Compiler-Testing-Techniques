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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 16, 1, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(16, 32, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(32, 32, 1, stride=1, padding=0)
        self.conv5 = torch.nn.Conv2d(32, 64, 1, stride=1, padding=0)
        self.conv6 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=0)
        self.conv7 = torch.nn.Conv2d(64, 64, 1, stride=1, padding=0)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        v5 = self.conv5(v4)
        v6 = self.conv6(v5)
        v7 = self.conv7(v6)
        v8 = v1.add(v6)
        v9 = v3 - v6
        v10 = torch.conv_transpose2d(v2, v7, padding=0, stride=1, groups=1)
        v11 = torch.cat([v5, v6, v7, v8, v9, v10], dim=1)
        return v11



func = Model().to('cpu')


x1 = torch.randn(1, 3, 32, 32)

x2 = torch.randn(1, 3, 32, 32)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (64) at non-singleton dimension 1

jit:
Failed running call_method add(*(FakeTensor(..., size=(1, 8, 17, 17)), FakeTensor(..., size=(1, 64, 17, 17))), **{}):
Attempting to broadcast a dimension of length 64 at -3! Mismatching argument at index 1 had torch.Size([1, 64, 17, 17]); but expected shape should be broadcastable to [1, 8, 17, 17]

from user code:
   File "<string>", line 33, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv = torch.nn.Conv2d(40, 64, 5, stride=1, padding=2)
        self.avgpool = torch.nn.AvgPool2d(7, stride=1)
        self.conv_1 = torch.nn.Conv2d(64, 128, 1, stride=1)
        self.conv_2 = torch.nn.Conv2d(128, 256, 1, stride=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.avgpool(v1)
        v3 = self.conv_1(v2)
        v4 = self.conv_2(v3)
        v5 = torch.add(v1, v4)
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 40, 45, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (58) at non-singleton dimension 3

jit:
Failed running call_function <built-in method add of type object at 0x76a9a2596ec0>(*(FakeTensor(..., size=(1, 64, 45, 64)), FakeTensor(..., size=(1, 256, 39, 58))), **{}):
Attempting to broadcast a dimension of length 58 at -1! Mismatching argument at index 1 had torch.Size([1, 256, 39, 58]); but expected shape should be broadcastable to [1, 64, 45, 64]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
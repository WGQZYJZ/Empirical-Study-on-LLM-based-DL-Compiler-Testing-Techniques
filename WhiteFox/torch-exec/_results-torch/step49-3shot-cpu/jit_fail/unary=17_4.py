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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(3, 32, 3, padding=1, stride=2)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(32, 16, 2, padding=0, stride=1)
        self.max_pool = torch.nn.MaxPool2d(2, stride=1)
        self.avg_pool = torch.nn.AvgPool2d(2, stride=1)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        v2 = self.relu(v1)
        v3 = self.conv_transpose_2(v2)
        v4 = self.relu(v3)
        v5 = self.max_pool(v4)
        v6 = self.avg_pool(v5)
        v7 = torch.add(v4, v6)
        v8 = torch.add(v7, v1)
        v9 = torch.sigmoid(v8)
        return v9



func = Model().to('cpu')


x1 = torch.randn(1, 3, 128, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (62) at non-singleton dimension 3

jit:
Failed running call_function <built-in method add of type object at 0x7c0a25b96ec0>(*(FakeTensor(..., size=(1, 16, 256, 64)), FakeTensor(..., size=(1, 16, 254, 62))), **{}):
Attempting to broadcast a dimension of length 62 at -1! Mismatching argument at index 1 had torch.Size([1, 16, 254, 62]); but expected shape should be broadcastable to [1, 16, 256, 64]

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv = torch.nn.ConvTranspose2d(8, 32, 1, stride=1, padding=0)
        self.conv1 = torch.nn.ConvTranspose2d(32, 64, 1, stride=1, padding=0)
        self.conv2 = torch.nn.ConvTranspose2d(64, 128, 1, stride=1, padding=0)
        self.conv3 = torch.nn.ConvTranspose2d(256, 2, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = self.conv1(v2)
        v4 = torch.max(v2, v3)
        v5 = torch.cat((v3, x1), dim=1)
        v6 = torch.max(v5, self.conv2(v4))
        v7 = self.conv3(v6)
        v8 = torch.sigmoid(v7)
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 8, 128, 128)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (32) must match the size of tensor b (64) at non-singleton dimension 1

jit:
Failed running call_function <built-in method max of type object at 0x7f3a51f96ec0>(*(FakeTensor(..., size=(1, 32, 128, 128)), FakeTensor(..., size=(1, 64, 128, 128))), **{}):
Attempting to broadcast a dimension of length 64 at -3! Mismatching argument at index 1 had torch.Size([1, 64, 128, 128]); but expected shape should be broadcastable to [1, 32, 128, 128]

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv0 = torch.nn.ConvTranspose2d(225, 257, 1, padding=0, stride=1)
        self.conv1 = torch.nn.ConvTranspose2d(257, 225, 1, padding=0, stride=1, dilation=3)
        self.conv2 = torch.nn.ConvTranspose2d(225, 225, 1, padding=0, stride=1)

    def forward(self, x1):
        v1 = torch.relu(x1)
        v2 = self.conv0(v1)
        v3 = torch.tanh(v2)
        v4 = self.conv1(v3)
        v5 = torch.sigmoid(v4)
        v6 = self.conv2(v5)
        v7 = torch.tanh(v6)
        v8 = torch.max_pool2d(v7, 2, stride=1)
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 225, 16384, 1)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given input size: (225x16384x1). Calculated output size: (225x16383x0). Output size is too small

jit:
Failed running call_function <built-in method max_pool2d of type object at 0x78ac2fb96ec0>(*(FakeTensor(..., size=(1, 225, s1, 1)), 2), **{'stride': 1}):
Given input size: (225xs1x1). Calculated output size: (225xs1 - 1x0). Output size is too small

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
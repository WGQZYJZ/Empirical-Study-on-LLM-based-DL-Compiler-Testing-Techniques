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
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv2(v2)
        v4 = torch.sigmoid(v3)
        x5 = torch.randn(1, 32, 64, 64)
        v5 = self.conv1(x5)
        v6 = torch.sigmoid(v5)
        x7 = torch.randn(1, 64, 64, 64)
        v7 = torch.sigmoid(v7)
        x8 = torch.cat((x2, v5, v7), 1)
        v8 = self.conv2(x8)
        v9 = torch.sigmoid(v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 3, 3, 3], expected input[1, 32, 64, 64] to have 3 channels, but got 32 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., size=(1, 32, 64, 64)),), **{}):
Given groups=1, weight of size [32, 3, 3, 3], expected input[1, 32, 64, 64] to have 3 channels, but got 32 channels instead

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
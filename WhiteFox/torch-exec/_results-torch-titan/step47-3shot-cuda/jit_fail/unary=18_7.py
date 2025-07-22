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
        self.conv01 = torch.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, stride=2, padding=1)
        self.conv02 = torch.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, stride=2, padding=1)
        self.conv03 = torch.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=2, padding=1)
        self.conv04 = torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=2, padding=1)
        self.conv05 = torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=8, stride=2, padding=1)
        self.conv06 = torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=8, stride=2, padding=1)
        self.conv1 = torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv01(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv02(v2)
        v4 = torch.sigmoid(v3)
        v5 = self.conv03(v4)
        v6 = torch.sigmoid(v5)
        v7 = self.conv04(v6)
        v8 = torch.sigmoid(v7)
        v9 = self.conv05(v8)
        v10 = torch.sigmoid(v9)
        v11 = self.conv06(v10)
        v12 = torch.sigmoid(v11)
        v13 = self.conv1(v12)
        v14 = torch.sigmoid(v13)
        v15 = self.conv2(v14)
        v16 = torch.sigmoid(v15)
        return v16




func = Model().to('cuda')



x1 = torch.randn(1, 32, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (6 x 6). Kernel size: (8 x 8). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv05(*(FakeTensor(..., device='cuda:0', size=(1, 64, 4, 4)),), **{}):
Calculated padded input size per channel: (6 x 6). Kernel size: (8 x 8). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 37, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=16, stride=16, padding=0)
        self.conv2 = torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=16, stride=8, padding=0)
        self.conv3 = torch.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=16, stride=8, padding=0)
        self.conv4 = torch.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=16, stride=8, padding=0)
        self.conv5 = torch.nn.Conv2d(in_channels=64, out_channels=64, kernel_size=16, stride=8, padding=0)
        self.conv6 = torch.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=16, stride=8, padding=0)
        self.conv7 = torch.nn.Conv2d(in_channels=128, out_channels=64, kernel_size=16, stride=8, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        v5 = self.conv5(v4)
        v6 = self.conv6(v5)
        v7 = self.conv7(v6)
        v8 = torch.sigmoid(v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 3, 512, 512)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (3 x 3). Kernel size: (16 x 16). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv3(*(FakeTensor(..., device='cuda:0', size=(1, 64, 3, 3)),), **{}):
Calculated padded input size per channel: (3 x 3). Kernel size: (16 x 16). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
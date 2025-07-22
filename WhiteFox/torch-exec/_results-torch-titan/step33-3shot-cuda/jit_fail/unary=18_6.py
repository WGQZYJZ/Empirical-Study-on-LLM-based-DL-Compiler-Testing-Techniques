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
        self.conv1 = torch.nn.Conv2d(64, 128, kernel_size=1, stride=1, padding=0, bias=False)
        self.bn1 = torch.nn.BatchNorm2d(num_features=128)
        self.conv2 = torch.nn.Conv2d(128, 256, kernel_size=2, stride=1, padding=0, dilation=1, groups=1, bias=False)
        self.bn2 = torch.nn.BatchNorm2d(num_features=256, eps=1e-05)
        self.conv3 = torch.nn.Conv2d(256, 256, kernel_size=2, stride=1, padding=0, dilation=1, groups=1, bias=False)
        self.bn3 = torch.nn.BatchNorm2d(num_features=256, eps=1e-05)
        self.conv4 = torch.nn.Conv2d(256, 512, kernel_size=2, stride=1, padding=0, dilation=1, groups=1, bias=False)
        self.bn4 = torch.nn.BatchNorm2d(num_features=512, eps=1e-05)

    def forward(self, x1):
        v1 = self.conv1(input=x1)
        v2 = self.bn1(v1)
        v3 = torch.sigmoid(v2)
        v4 = self.conv2(input=v3)
        v5 = self.bn2(v4)
        v6 = torch.sigmoid(v5)
        v7 = self.conv3(input=v6)
        v8 = self.bn3(v7)
        v9 = torch.sigmoid(v8)
        v10 = self.conv4(input=v9)
        v11 = self.bn4(v10)
        v12 = torch.sigmoid(v11)
        return v12




func = Model().to('cuda')



x1 = torch.randn(1, 64, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 1). Kernel size: (2 x 2). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv3(*(), **{'input': FakeTensor(..., device='cuda:0', size=(1, 256, 1, 1))}):
Calculated padded input size per channel: (1 x 1). Kernel size: (2 x 2). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
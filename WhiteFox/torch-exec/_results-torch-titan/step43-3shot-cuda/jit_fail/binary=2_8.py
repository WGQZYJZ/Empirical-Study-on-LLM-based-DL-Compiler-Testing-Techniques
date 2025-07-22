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
        self.conv = torch.nn.Conv2d(64, 128, 16, stride=16, padding=16)
        self.relu1 = torch.nn.ReLU(inplace=False)
        self.conv1 = torch.nn.Conv2d(128, 64, 1, stride=1, padding=0)
        self.relu2 = torch.nn.ReLU(inplace=False)
        self.conv2 = torch.nn.Conv2d(64, 32, 1, stride=1, padding=0)
        self.relu3 = torch.nn.ReLU(inplace=False)
        self.conv3 = torch.nn.Conv2d(32, 16, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.relu1(self.conv(x1))
        v2 = self.relu2(self.conv1(v1))
        v3 = self.conv2(v2)
        v4 = self.relu3(self.conv3(v3))
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 128, 128)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [128, 64, 16, 16], expected input[1, 3, 128, 128] to have 64 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 128, 128)),), **{}):
Given groups=1, weight of size [128, 64, 16, 16], expected input[1, 3, 128, 128] to have 64 channels, but got 3 channels instead

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
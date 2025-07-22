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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3)
        self.conv2 = torch.nn.Conv2d(in_channels=1, out_channels=1, kernel_size=1)
        self.conv3 = torch.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3)
        self.conv4 = torch.nn.Conv2d(in_channels=1, out_channels=1, kernel_size=1)
        self.conv5 = torch.nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3)
        self.conv6 = torch.nn.Conv2d(in_channels=1, out_channels=1, kernel_size=1)
        self.maxpool = torch.nn.MaxPool2d(2)

    def forward(self, x1):
        x = self.maxpool(F.relu(self.conv1(x1)))
        x = self.maxpool(F.relu(self.conv2(x)))
        x = self.maxpool(F.relu(self.conv3(x)))
        x = self.maxpool(F.relu(self.conv4(x)))
        x = self.maxpool(F.relu(self.conv5(x)))
        x = self.maxpool(F.relu(self.conv6(x)))
        x = torch.sigmoid(x)
        x = self.maxpool(F.relu(x))
        return x




func = Model().to('cuda')



x1 = torch.rand(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 32, 31, 31] to have 1 channels, but got 32 channels instead

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 32, 31, 31)),), **{}):
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 32, 31, 31] to have 1 channels, but got 32 channels instead

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
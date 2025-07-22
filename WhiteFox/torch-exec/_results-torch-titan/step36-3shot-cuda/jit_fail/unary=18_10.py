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
        self.conv1 = torch.nn.Conv2d(in_channels=64, out_channels=96, kernel_size=5, stride=2, padding=2, bias=False)
        self.conv2 = torch.nn.Conv2d(in_channels=96, out_channels=128, kernel_size=3, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(in_channels=128, out_channels=192, kernel_size=3, stride=1, padding=1, bias=False)
        self.fc1 = torch.nn.Linear(192, 10)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v5 = torch.flatten(v3, 1)
        v6 = self.fc1(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(128, 3, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [96, 64, 5, 5], expected input[128, 3, 32, 32] to have 64 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv1(*(FakeTensor(..., device='cuda:0', size=(128, 3, 32, 32)),), **{}):
Given groups=1, weight of size [96, 64, 5, 5], expected input[128, 3, 32, 32] to have 64 channels, but got 3 channels instead

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.pool = torch.nn.MaxPool2d(3, stride=1, padding=1)
        self.relu = torch.nn.ReLU(inplace=True)
        self.conv = torch.nn.Conv2d(3, 384, 1, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(1, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.avgpool = torch.nn.AvgPool2d(2, stride=1, padding=0)

    def forward(self, x1):
        t1 = self.pool(x1)
        t2 = self.relu(t1)
        t3 = self.conv(t2)
        t4 = (3 + t3)
        t5 = torch.clamp_min(t4, 0)
        t6 = torch.clamp_max(t5, 6)
        t7 = (t6 / 6)
        t8 = self.bn(t7)
        t9 = self.avgpool(t8)
        return t9.unsqueeze((- 1))




func = Model().to('cuda')



x1 = torch.randn(2, 1, 28, 28)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [384, 3, 1, 1], expected input[2, 1, 28, 28] to have 3 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(2, 1, 28, 28)),), **{}):
Given groups=1, weight of size [384, 3, 1, 1], expected input[2, 1, 28, 28] to have 3 channels, but got 1 channels instead

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
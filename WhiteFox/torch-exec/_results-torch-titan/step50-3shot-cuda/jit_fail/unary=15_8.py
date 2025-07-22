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
        self.conv1 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(3, 216, 2048, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(216, 32, 3, stride=2, padding=1)
        self.conv4 = torch.nn.Conv2d(32, 128, 5, stride=1, padding=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v2)
        v4 = torch.relu(v3)
        v5 = self.conv3(v4)
        v6 = torch.relu(v5)
        v7 = self.conv4(v6)
        v8 = torch.relu(v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 3, 288, 288)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (288 x 288). Kernel size: (2048 x 2048). Kernel size can't be greater than actual input size

jit:
Failed running call_module L__self___conv2(*(FakeTensor(..., device='cuda:0', size=(1, 3, 288, 288)),), **{}):
Calculated padded input size per channel: (288 x 288). Kernel size: (2048 x 2048). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv = torch.nn.Conv2d(128, 512, 1, stride=1, padding=1)
        self.conv_1 = torch.nn.Conv2d(256, 384, 1, stride=3, padding=1)
        self.conv_2 = torch.nn.Conv2d(64, 128, 1, stride=3, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.sigmoid()
        v4 = self.conv_1(v2)
        v5 = (v4 * v2)
        v6 = v5.tanh()
        v7 = v6.sigmoid()
        v8 = (v1 * v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 64, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [512, 128, 1, 1], expected input[1, 64, 32, 32] to have 128 channels, but got 64 channels instead

jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 64, 32, 32)),), **{}):
Given groups=1, weight of size [512, 128, 1, 1], expected input[1, 64, 32, 32] to have 128 channels, but got 64 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
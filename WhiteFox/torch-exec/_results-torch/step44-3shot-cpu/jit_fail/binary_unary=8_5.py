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
        self.conv = torch.nn.Conv2d(3, 32, 1, stride=1, padding=1)

    def forward(self, x1):
        x11 = torch.nn.functional.interpolate(x1, size=128, scale_factor=1, mode='nearest', align_corners=False)
        v1 = self.conv(x11)
        x21 = torch.nn.functional.interpolate(x1, size=64, scale_factor=1, mode='nearest', align_corners=False)
        v2 = self.conv(x21)
        x31 = torch.nn.functional.interpolate(x1, size=32, scale_factor=1, mode='nearest', align_corners=False)
        v3 = self.conv(x31)
        x41 = torch.nn.functional.interpolate(x11, size=128, scale_factor=1, mode='nearest', align_corners=False)
        v4 = self.conv(x41)
        v5 = self.conv(x31)
        v6 = self.conv(x21)
        v7 = v1 + v2 + v3 + v4 + v5 + v6
        v8 = torch.relu(v7)
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64, requires_grad=True)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
align_corners option can only be set with the interpolating modes: linear | bilinear | bicubic | trilinear

jit:
Failed running call_function <function interpolate at 0x76c6476440d0>(*(FakeTensor(..., size=(1, s0, s1, s2)),), **{'size': 128, 'scale_factor': 1, 'mode': 'nearest', 'align_corners': False}):
align_corners option can only be set with the interpolating modes: linear | bilinear | bicubic | trilinear

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
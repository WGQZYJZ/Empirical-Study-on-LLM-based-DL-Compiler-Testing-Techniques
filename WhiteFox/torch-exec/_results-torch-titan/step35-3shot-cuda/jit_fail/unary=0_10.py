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
        self.conv = torch.nn.Conv2d(128, 64, 1, stride=2, padding=1)
        self.upsample = torch.nn.Upsample(scale_factor=4.0, mode='nearest', align_corners=True)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.upsample(v1)
        v3 = (v2 * 0.5)
        v4 = (v2 * v2)
        v5 = (v4 * v2)
        v6 = (v5 * 0.044715)
        v7 = (v2 + v6)
        v8 = (v7 * 0.7978845608028654)
        v9 = torch.tanh(v8)
        v10 = (v9 + 1)
        v11 = (v3 * v10)
        return v11




func = Model().to('cuda')



x1 = torch.randn(1, 128, 4, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
align_corners option can only be set with the interpolating modes: linear | bilinear | bicubic | trilinear

jit:
Failed running call_module L__self___upsample(*(FakeTensor(..., device='cuda:0', size=(1, 64, 3, 4)),), **{}):
align_corners option can only be set with the interpolating modes: linear | bilinear | bicubic | trilinear

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
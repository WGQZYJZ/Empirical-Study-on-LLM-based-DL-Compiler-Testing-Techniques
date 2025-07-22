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
        v3 = v2 * 0.5
        v4 = v2 * v2
        v5 = v4 * v2
        v6 = v5 * 0.044715
        v7 = v2 + v6
        v8 = v7 * 0.7978845608028654
        v9 = torch.tanh(v8)
        v10 = v9 + 1
        v11 = v3 * v10
        return v11



func = Model().to('cpu')


x1 = torch.randn(1, 128, 4, 5)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
align_corners option can only be set with the interpolating modes: linear | bilinear | bicubic | trilinear

jit:
Failed running call_function <function interpolate at 0x714f5c1990d0>(*(FakeTensor(..., size=(1, 64, (((s1 + 1)//2)) + 1, (((s2 + 1)//2)) + 1)), None, 4.0, 'nearest', True), **{'recompute_scale_factor': None}):
align_corners option can only be set with the interpolating modes: linear | bilinear | bicubic | trilinear

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/upsampling.py", line 172, in forward
    return F.interpolate(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
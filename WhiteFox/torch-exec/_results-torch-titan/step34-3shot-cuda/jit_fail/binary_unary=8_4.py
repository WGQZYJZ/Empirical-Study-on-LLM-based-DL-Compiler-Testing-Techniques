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
        self.conv = torch.nn.Conv2d(3, 8, (3, 5), stride=(2, 3), padding=(1, 2))
        self.avgpool = torch.nn.AdaptiveAvgPool2d((1, 1))

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.avgpool(v1)
        v3 = torch.nn.functional.interpolate(v2, scale_factor=2, mode='nearest', align_corners=False)
        v4 = (v1 + v3)
        return torch.nn.functional.relu(v4)




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
align_corners option can only be set with the interpolating modes: linear | bilinear | bicubic | trilinear

jit:
Failed running call_function <function interpolate at 0x7db32b2f7430>(*(FakeTensor(..., device='cuda:0', size=(1, 8, 1, 1)),), **{'scale_factor': 2, 'mode': 'nearest', 'align_corners': False}):
align_corners option can only be set with the interpolating modes: linear | bilinear | bicubic | trilinear

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
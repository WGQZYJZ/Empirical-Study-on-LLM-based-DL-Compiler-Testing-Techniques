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

    def __init__(self, min_value=(- 0.7100000381469727), max_value=2.0):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(512, 2, 1, stride=1, padding=2)
        self.gelu = torch.nn.GELU()
        self.upsample = torch.nn.Upsample(scale_factor=98.0, mode='nearest')
        self.conv_transpose1 = torch.nn.ConvTranspose2d(1, 8, 3, stride=1, padding=0)
        self.conv = torch.nn.Conv2d(4, 1024, 3, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.gelu(v1)
        v3 = self.upsample(v2)
        v4 = self.conv_transpose1(v2)
        v5 = torch.mul(v4, v3)
        v6 = self.conv(v5)
        v7 = self.gelu(v6)
        v8 = self.conv_transpose(v7)
        v9 = torch.mul(x1, v8)
        v10 = torch.clamp_min(v9, self.min_value)
        v11 = torch.clamp_max(v10, self.max_value)
        v12 = self.conv_transpose1(v11)
        v13 = torch.mul(v12, v6)
        v14 = torch.clamp_min(v13, self.min_value)
        v15 = torch.clamp_max(v14, self.max_value)
        v16 = self.conv(v7)
        v17 = torch.mul(v15, v16)
        v18 = torch.clamp_min(v17, self.min_value)
        v19 = torch.clamp_max(v18, self.max_value)
        return v19




func = Model().to('cuda')



x1 = torch.randn(1, 512, 8, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 8, 3, 3], expected input[1, 2, 4, 4] to have 1 channels, but got 2 channels instead

jit:
Failed running call_module L__self___conv_transpose1(*(FakeTensor(..., device='cuda:0', size=(1, 2, 4, 4)),), **{}):
Given transposed=1, weight of size [1, 8, 3, 3], expected input[1, 2, 4, 4] to have 1 channels, but got 2 channels instead

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
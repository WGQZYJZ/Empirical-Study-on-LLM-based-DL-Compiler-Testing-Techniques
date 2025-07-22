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

    def __init__(self, min_value=(- 22.495158697470075), max_value=28.411253885560395):
        super().__init__()
        self.conv2d = torch.nn.Conv2d(3, 1, 5, stride=5, padding=5)
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 3, stride=2, padding=1)
        self.relu6 = torch.nn.ReLU6()
        self.adaptive_avg_pool2d = torch.nn.AdaptiveAvgPool2d(output_size=(7, 7))
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = self.conv_transpose(v1)
        v3 = torch.clamp_min(v2, self.min_value)
        v4 = torch.clamp_max(v3, self.max_value)
        v5 = self.relu6(v4)
        v6 = self.adaptive_avg_pool2d(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [3, 8, 3, 3], expected input[1, 1, 14, 14] to have 3 channels, but got 1 channels instead

jit:
Failed running call_module L__self___conv_transpose(*(FakeTensor(..., device='cuda:0', size=(1, 1, 14, 14)),), **{}):
Given transposed=1, weight of size [3, 8, 3, 3], expected input[1, 1, 14, 14] to have 3 channels, but got 1 channels instead

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
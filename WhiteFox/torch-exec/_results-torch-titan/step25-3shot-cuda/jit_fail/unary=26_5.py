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

    def __init__(self, stride, out_channels, kernel_size, negative_slope, padding, dilation, bias):
        super().__init__()
        self.conv_transpose2d = torch.nn.ConvTranspose2d(in_channels=3, out_channels=out_channels, kernel_size=kernel_size, stride=stride, padding=padding, dilation=dilation, bias=bias)
        self.conv2d = torch.nn.Conv2d(in_channels=1, out_channels=1, kernel_size=1, stride=1, padding=1, dilation=1, bias=bias)
        self.relu = torch.nn.ReLU()
        self.negative_slope = negative_slope

    def forward(self, x4):
        v1 = self.conv_transpose2d(x4)
        v2 = self.conv2d(x4)
        v3 = self.relu(v2)
        v4 = (v3 > 0)
        v5 = (v3 * self.negative_slope)
        v6 = torch.where(v4, v3, v5)
        return v6




stride = 2


out_channels = 4


kernel_size = 3


negative_slope = 0.001


padding = 2


dilation = 4


bias = True


func = Model(stride, out_channels, kernel_size, negative_slope, padding, dilation, bias).to('cuda')



x4 = torch.randn(8, 3, 8, 8)


test_inputs = [x4]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 1, 1], expected input[8, 3, 8, 8] to have 1 channels, but got 3 channels instead

jit:
Failed running call_module L__self___conv2d(*(FakeTensor(..., device='cuda:0', size=(8, 3, 8, 8)),), **{}):
Given groups=1, weight of size [1, 1, 1, 1], expected input[8, 3, 8, 8] to have 1 channels, but got 3 channels instead

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
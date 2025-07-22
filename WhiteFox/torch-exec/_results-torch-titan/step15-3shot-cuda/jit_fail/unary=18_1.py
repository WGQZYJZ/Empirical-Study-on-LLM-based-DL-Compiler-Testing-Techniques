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



class model(nn.Module):

    def __init__(self, in_channels, out_channels, kernel_size, stride, padding):
        super(model, self).__init__()
        self.conv_block = nn.Sequential(nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding), nn.BatchNorm2d(out_channels), nn.Sigmoid())
        self.conv = torch.nn.Conv2d(in_channels, out_channels=128, kernel_size=1, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.conv_block(v1)
        return v2




in_channels = 3


out_channels = 128


kernel_size = 1


stride = 1


padding = 1


func = model(in_channels, out_channels, kernel_size, stride, padding).to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [128, 3, 1, 1], expected input[1, 128, 66, 66] to have 3 channels, but got 128 channels instead

jit:
Failed running call_module L__self___conv_block_0(*(FakeTensor(..., device='cuda:0', size=(1, 128, 66, 66)),), **{}):
Given groups=1, weight of size [128, 3, 1, 1], expected input[1, 128, 66, 66] to have 3 channels, but got 128 channels instead

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
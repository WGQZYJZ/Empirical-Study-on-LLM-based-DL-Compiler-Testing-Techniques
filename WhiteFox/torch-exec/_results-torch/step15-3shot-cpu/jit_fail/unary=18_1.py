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

func = model(in_channels, out_channels, kernel_size, stride, padding).to('cpu')


x = torch.randn(1, 3, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [128, 3, 1, 1], expected input[1, 128, 66, 66] to have 3 channels, but got 128 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x72223cb96ec0>(*(FakeTensor(..., size=(1, 128, 66, 66)), Parameter(FakeTensor(..., size=(128, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(128,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [128, 3, 1, 1], expected input[1, 128, 66, 66] to have 3 channels, but got 128 channels instead

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
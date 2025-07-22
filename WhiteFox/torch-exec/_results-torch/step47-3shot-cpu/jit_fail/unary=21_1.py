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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.pool2d = torch.nn.MaxPool2d(kernel_size=3, stride=3, padding=0)
        self.conv = torch.nn.Conv2d(150, 80, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        self.sigmoid0 = torch.nn.Sigmoid()
        self.conv2 = torch.nn.Conv2d(80, 55, kernel_size=3, stride=1, padding=1)
        self.conv2d1 = torch.nn.Conv2d(384, 176, kernel_size=(3, 13), stride=(3, 1), padding=(0, 0), bias=False)
        self.sigmoid = torch.nn.Sigmoid()
        self.conv2d0_ = torch.nn.Conv2d(16, 16, kernel_size=3, stride=1, padding=1, dilation=1)
        self.conv2d1 = torch.nn.Conv2d(16, 16, kernel_size=5, stride=1, padding=2, dilation=2)
        self.conv2d3_ = torch.nn.Conv2d(16, 16, kernel_size=3, stride=1, padding=1, dilation=1)
        self.conv2d4 = torch.nn.Conv2d(16, 16, kernel_size=3, stride=1, padding=2, dilation=2, groups=2)

    def forward(self, x0):
        x14 = self.conv(self.conv(x0))
        x10 = self.conv(self.pool2d(x0))
        x13 = self.conv2d0_(x10)
        x15 = self.sigmoid0(self.conv2(x14))
        x12 = self.conv2d3_(x14)
        x9 = self.conv2d1(x10)
        x11 = self.conv2d3_(x14)
        x8 = self.conv2d1(x10)
        x7 = self.conv2d3_(x14)
        x9 = self.conv2d1(x9)
        x11 = self.conv2d3_(x11)
        x8 = self.sigmoid(self.conv2d1(x8))
        x7 = self.sigmoid(self.conv2d1(x7))
        x4 = self.conv2d4(self.conv(x0))
        return self.conv2d1(x9).transpose(3, 1).transpose(3, 2)



func = ModelTanh().to('cpu')


x0 = torch.randn(893, 3, 61, 150)

test_inputs = [x0]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [80, 150, 3, 3], expected input[893, 3, 61, 150] to have 150 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7583bc396ec0>(*(FakeTensor(..., size=(893, 3, 61, 150)), Parameter(FakeTensor(..., size=(80, 150, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(80,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [80, 150, 3, 3], expected input[893, 3, 61, 150] to have 150 channels, but got 3 channels instead

from user code:
   File "<string>", line 29, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
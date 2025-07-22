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

    def __init__(self, min, max):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 16, 5, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 2, 3, padding=2)
        self.conv3 = torch.nn.Conv2d(2, 8, 5, padding=1)
        self.conv4 = torch.nn.Conv2d(8, 16, 3, padding=2)
        self.conv5 = torch.nn.Conv2d(16, 2, 3, padding=1)
        self.conv6 = torch.nn.Conv2d(16, 2, 1, padding=1)
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        v5 = self.conv5(v4)
        v6 = self.conv6(v5)
        v7 = torch.clamp_min(v6, self.min)
        v8 = torch.clamp_max(v7, self.max)
        return v8


min = 0.5
max = 1.0

func = Model(min, max).to('cpu')


x1 = torch.randn(1, 2, 320, 103)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 16, 1, 1], expected input[1, 2, 320, 103] to have 16 channels, but got 2 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x78b9e7396ec0>(*(FakeTensor(..., size=(1, 2, 320, 103)), Parameter(FakeTensor(..., size=(2, 16, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [2, 16, 1, 1], expected input[1, 2, 320, 103] to have 16 channels, but got 2 channels instead

from user code:
   File "<string>", line 32, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
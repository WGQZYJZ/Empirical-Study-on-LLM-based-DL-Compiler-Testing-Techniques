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

class Model(nn.Module):

    def __init__(self, in_channels, kernel_size, stride, output_features):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels, 16, kernel_size, stride)
        self.conv2 = nn.Conv2d(16, 8, kernel_size, stride)
        self.conv3 = nn.Conv2d(8, 4, kernel_size, stride)
        self.conv4 = nn.Conv2d(4, output_features, kernel_size, stride)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = torch.sigmoid(v1)
        v3 = self.conv2(v2)
        v4 = torch.sigmoid(v3)
        v5 = self.conv3(v4)
        v6 = torch.sigmoid(v5)
        v7 = self.conv4(v6)
        v8 = torch.sigmoid(v7)
        return v8


in_channels = 64
kernel_size = 2
stride = 2
output_features = 1

func = Model(in_channels, kernel_size, stride, output_features).to('cpu')


x = torch.randn(1, 3, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 64, 2, 2], expected input[1, 3, 64, 64] to have 64 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7971b2396ec0>(*(FakeTensor(..., size=(1, 3, 64, 64)), Parameter(FakeTensor(..., size=(16, 64, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (2, 2), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [16, 64, 2, 2], expected input[1, 3, 64, 64] to have 64 channels, but got 3 channels instead

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
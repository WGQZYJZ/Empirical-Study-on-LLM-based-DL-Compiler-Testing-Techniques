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

    def __init__(self, min_value=-2, max_value=-8):
        super().__init__()
        self.conv2d = torch.nn.Conv2d(1, 3, (3, 5))
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 1, 3)
        self.sigmoid = torch.nn.Sigmoid()
        self.avgpool = torch.nn.AvgPool2d(1, stride=1, padding=2)
        self.batch_norm = torch.nn.BatchNorm1d(num_features=1, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(3, 1, 1)
        self.relu = torch.nn.ReLU()
        self.maxpool = torch.nn.MaxPool2d(3, stride=1, padding=2)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv2d(x1)
        v2 = self.maxpool(v1)
        v3 = self.conv_transpose(v2)
        v4 = self.batch_norm(v3)
        v5 = self.sigmoid(v4)
        v6 = self.avgpool(v5)
        v7 = self.conv_transpose2(v6)
        v8 = torch.clamp_max(v7, self.max_value)
        v9 = self.relu(v8)
        v10 = torch.clamp_min(v9, self.min_value)
        return v10



func = Model().to('cpu')


x1 = torch.randn(1, 1, 16, 16)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of effective kernel size, but got pad=2, kernel_size=3 and dilation=1

jit:
Failed running call_function <function boolean_dispatch.<locals>.fn at 0x7bebcd6a0ee0>(*(FakeTensor(..., size=(1, 3, 14, 12)), 3, 1, 2, 1), **{'ceil_mode': False, 'return_indices': False}):
pad should be at most half of effective kernel size, but got pad=2, kernel_size=3 and dilation=1

from user code:
   File "<string>", line 30, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/pooling.py", line 213, in forward
    return F.max_pool2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
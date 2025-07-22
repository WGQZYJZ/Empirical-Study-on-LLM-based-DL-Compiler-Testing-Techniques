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

    def __init__(self, min1, max1, min2, max2):
        super().__init__()
        self.t1_conv = torch.nn.Conv2d(1, 1, 1, stride=1, padding=0)
        self.t2_conv = torch.nn.Conv2d(2, 1, 1, stride=1, padding=0)
        self.t3_conv = torch.nn.Conv2d(2, 4, 2, stride=2, padding=0)
        self.t4_conv = torch.nn.Conv2d(1, 1, 3, stride=2, padding=0)
        self.min1 = min1
        self.max1 = max1
        self.min2 = min2
        self.max2 = max2

    def forward(self, x1):
        v1 = self.t1_conv(x1)
        v2 = torch.clamp_min(v1, self.min1)
        v3 = torch.clamp_max(v2, self.max1)
        v4 = self.t2_conv(v3)
        v5 = torch.clamp_min(v4, self.min2)
        v6 = torch.clamp_max(v5, self.max2)
        v7 = self.t3_conv(v6)
        v8 = self.t4_conv(v7)
        return v8


min1 = 0.8
max1 = 1
min2 = 0.1
max2 = 1

func = Model(min1, max1, min2, max2).to('cpu')


x1 = torch.randn(1, 1, 353, 512)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 2, 1, 1], expected input[1, 1, 353, 512] to have 2 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7027d7596ec0>(*(FakeTensor(..., size=(1, 1, 353, 512)), Parameter(FakeTensor(..., size=(1, 2, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [1, 2, 1, 1], expected input[1, 1, 353, 512] to have 2 channels, but got 1 channels instead

from user code:
   File "<string>", line 30, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv = torch.nn.Conv2d(16, 8, 3, stride=2, padding=1)
        self.bn = torch.nn.BatchNorm2d(8, eps=0.0003, momentum=0.99)
        self.min = min
        self.max = max

    def forward(self, x1):
        conv = self.conv(x1)
        bn = self.bn(conv)
        clamp_min = torch.clamp(bn, min=self.min)
        clamp_max = torch.clamp(clamp_min, max=self.max)
        return clamp_max


min = 1.0
max = 1.5

func = Model(min, max).to('cpu')


x1 = torch.tensor([-1.1, 0.8]).reshape(-1, 1, 1, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 16, 3, 3], expected input[1, 1, 1, 2] to have 16 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7bd14b796ec0>(*(FakeTensor(..., size=(1, 1, 1, 2)), Parameter(FakeTensor(..., size=(8, 16, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), (2, 2), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [8, 16, 3, 3], expected input[1, 1, 1, 2] to have 16 channels, but got 1 channels instead

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
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
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 4, 3, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(3, 4, 3, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(3, 1, 3, stride=1, padding=1)
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        v3 = self.conv3(x1)
        v4 = self.conv4(v3)
        v5 = self.conv5(v4)
        v6 = torch.clamp_min(v1, self.min)
        v7 = torch.clamp_min(v2, self.min)
        v8 = torch.clamp_min(v5, self.min)
        v9 = torch.clamp_max(v6, self.max)
        v10 = torch.clamp_max(v7, self.max)
        v11 = torch.clamp_max(v8, self.max)
        return v9


min = 42
max = 73

func = Model(min, max).to('cpu')


x1 = torch.randn(1, 3, 100, 100)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [4, 3, 3, 3], expected input[1, 4, 100, 100] to have 3 channels, but got 4 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7e3eaa796ec0>(*(FakeTensor(..., size=(1, 4, 100, 100)), Parameter(FakeTensor(..., size=(4, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(4,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [4, 3, 3, 3], expected input[1, 4, 100, 100] to have 3 channels, but got 4 channels instead

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
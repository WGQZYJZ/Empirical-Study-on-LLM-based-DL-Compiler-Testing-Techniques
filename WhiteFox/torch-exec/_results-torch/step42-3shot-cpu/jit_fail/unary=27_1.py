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
        self.conv = torch.nn.Conv2d(2, 1, 9, stride=5, padding=1)
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min)
        v3 = torch.clamp_max(v2, self.max)
        return v3


min = 0.7
max = 4.8

func = Model(min, max).to('cpu')


x1 = torch.randn(1, 2, 14, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (16 x 6). Kernel size: (9 x 9). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x705059596ec0>(*(FakeTensor(..., size=(1, 2, 14, 4)), Parameter(FakeTensor(..., size=(1, 2, 9, 9), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (5, 5), (1, 1), (1, 1), 1), **{}):
Calculated padded input size per channel: (16 x 6). Kernel size: (9 x 9). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
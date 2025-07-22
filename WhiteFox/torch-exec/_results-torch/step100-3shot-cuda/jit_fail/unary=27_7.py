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
        self.conv = torch.nn.Conv2d(255, 1, 64, stride=1, padding=0)
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min)
        v3 = torch.clamp_max(v2, self.max)
        return v3


min = 0.8
max = 1.9

func = Model(min, max).to('cuda')


x1 = torch.randn(255, 1, 1, 1)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 255, 64, 64], expected input[255, 1, 1, 1] to have 255 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x724c1bf96ec0>(*(FakeTensor(..., device='cuda:0', size=(s0, 1, 1, 1)), Parameter(FakeTensor(..., device='cuda:0', size=(1, 255, 64, 64), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(1,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [1, 255, 64, 64], expected input[s0, 1, 1, 1] to have 255 channels, but got 1 channels instead

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
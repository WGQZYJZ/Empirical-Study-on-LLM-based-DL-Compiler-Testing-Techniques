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

    def __init__(self, min_value=0.592785640239, max_value=0.0528118573668):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(1828, 526, 1, stride=3, padding=0)
        self.conv = torch.nn.Conv2d(508, 783, 1, stride=1, padding=0)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.conv(v3)
        return v4



func = Model().to('cuda')


x1 = torch.randn(1, 1828, 35, 35)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [783, 508, 1, 1], expected input[1, 526, 103, 103] to have 508 channels, but got 526 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x72af92996ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 526, 3*s1 - 2, 3*s2 - 2)), Parameter(FakeTensor(..., device='cuda:0', size=(783, 508, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., device='cuda:0', size=(783,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [783, 508, 1, 1], expected input[1, 526, 3*s1 - 2, 3*s2 - 2] to have 508 channels, but got 526 channels instead

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
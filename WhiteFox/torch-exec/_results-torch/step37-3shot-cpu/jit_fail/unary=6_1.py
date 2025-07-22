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

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)
        self.clamp_min_0 = torch.nn.ReLU6(inplace=True)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, 0)
        v3 = v1 * v2
        v4 = v3 / 6
        return v4



func = Model().to('cpu')


x1 = torch.randn(3, 8, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 3, 1, 1], expected input[3, 8, 64, 64] to have 3 channels, but got 8 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x702807d96ec0>(*(FakeTensor(..., size=(3, 8, 64, 64)), Parameter(FakeTensor(..., size=(3, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [3, 3, 1, 1], expected input[3, 8, 64, 64] to have 3 channels, but got 8 channels instead

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
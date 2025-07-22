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
        self.negative_slope = -0.92
        self.conv = torch.nn.Conv2d(4, 7, (4, 8), stride=7)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 < 0
        v3 = v1 * self.negative_slope
        v4 = v1 - v3
        v5 = torch.clamp(v4, self.negative_slope)
        v6 = torch.where(v2, v5, v4)
        return v6



func = Model().to('cpu')


x = torch.randn(5, 4, 2, 9, device='cpu')

test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2 x 9). Kernel size: (4 x 8). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7f044d596ec0>(*(FakeTensor(..., size=(s0, 4, 2, s2)), Parameter(FakeTensor(..., size=(7, 4, 4, 8), requires_grad=True)), Parameter(FakeTensor(..., size=(7,), requires_grad=True)), (7, 7), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (2 x s2). Kernel size: (4 x 8). Kernel size can't be greater than actual input size

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
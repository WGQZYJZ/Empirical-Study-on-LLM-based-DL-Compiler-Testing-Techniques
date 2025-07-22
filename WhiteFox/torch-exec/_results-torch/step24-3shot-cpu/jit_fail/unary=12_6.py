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
        self.conv = torch.nn.Conv2d(72, 13, 63, stride=8, padding=16, dilation=9)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.tanh()
        v3 = v2.mul(v1)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 72, 16, 16)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (48 x 48). Kernel size: (559 x 559). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x70e8ee996ec0>(*(FakeTensor(..., size=(1, 72, 16, 16)), Parameter(FakeTensor(..., size=(13, 72, 63, 63), requires_grad=True)), Parameter(FakeTensor(..., size=(13,), requires_grad=True)), (8, 8), (16, 16), (9, 9), 1), **{}):
Calculated padded input size per channel: (48 x 48). Kernel size: (559 x 559). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
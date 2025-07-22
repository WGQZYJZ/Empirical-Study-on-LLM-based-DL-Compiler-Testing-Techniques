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

class ConvModel(torch.nn.Module):

    def __init__(self, in_channel, out_channel):
        super().__init__()
        self._conv = torch.nn.Conv2d(in_channel, out_channel, kernel_size=3, stride=2, padding=1)

    def forward(self, x):
        x1 = self._conv(x)
        x2 = self._conv(x)
        x3 = self._conv(x)
        return (x1, x2, x3)


in_channel = 1
out_channel = 1

func = ConvModel(in_channel, out_channel).to('cpu')


x1 = torch.randn(1, 56, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 3, 3], expected input[1, 56, 64, 64] to have 1 channels, but got 56 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7cd20dd96ec0>(*(FakeTensor(..., size=(1, 56, 64, 64)), Parameter(FakeTensor(..., size=(1, 1, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (2, 2), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [1, 1, 3, 3], expected input[1, 56, 64, 64] to have 1 channels, but got 56 channels instead

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
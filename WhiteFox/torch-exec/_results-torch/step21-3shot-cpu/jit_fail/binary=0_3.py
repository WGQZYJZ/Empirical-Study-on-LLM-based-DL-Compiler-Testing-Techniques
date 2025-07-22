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

    def __init__(self, in_ch, out_ch, kernel_size, in_size, out_size, bias=None, dilation=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(in_ch, out_ch, kernel_size, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(2, 2, 1, stride=2, padding=2)

    def forward(self, x1=None, other=None):
        v1 = self.conv(x1)
        y1 = self.conv2(other)
        v2 = v1 + y1
        return v2


in_ch = 1
out_ch = 1
kernel_size = 1
in_size = 1
out_size = 1

func = Model(in_ch, out_ch, kernel_size, in_size, out_size).to('cpu')


x1 = torch.randn(1, 5, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 5, 64, 64] to have 1 channels, but got 5 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7cd20dd96ec0>(*(FakeTensor(..., size=(1, 5, 64, 64)), Parameter(FakeTensor(..., size=(1, 1, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 5, 64, 64] to have 1 channels, but got 5 channels instead

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
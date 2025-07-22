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
        self.conv1 = torch.nn.Conv2d(in_channels=1, out_channels=64, kernel_size=7, stride=7)
        self.conv2 = torch.nn.Conv2d(64, 64, 7, stride=7)
        self.conv3 = torch.nn.Conv2d(64, 64, 7, stride=7)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = torch.sigmoid(v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 1, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 1). Kernel size: (7 x 7). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x79843ed96ec0>(*(FakeTensor(..., size=(1, 64, 1, 1)), Parameter(FakeTensor(..., size=(64, 64, 7, 7), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True)), (7, 7), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (1 x 1). Kernel size: (7 x 7). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
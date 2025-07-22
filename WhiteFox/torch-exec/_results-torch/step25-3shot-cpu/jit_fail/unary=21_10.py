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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1d = torch.nn.Conv1d(in_channels=2, out_channels=2, kernel_size=2, stride=1, padding=1)
        self.conv2d = torch.nn.Conv2d(in_channels=1, out_channels=3, kernel_size=2, stride=1, padding=0)

    def forward(self, x):
        x1 = self.conv2d(x)
        x2 = torch.tanh(x1)
        x3 = self.conv1d(x2)
        x4 = torch.tanh(x3)
        return x4



func = ModelTanh().to('cpu')


x = torch.randn(1, 1, 100)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 100). Kernel size: (2 x 2). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7c9244396ec0>(*(FakeTensor(..., size=(1, 1, 100)), Parameter(FakeTensor(..., size=(3, 1, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (1 x 100). Kernel size: (2 x 2). Kernel size can't be greater than actual input size

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
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

class model(torch.nn.Module):

    def __init__(self):
        super(model, self).__init__()
        self.conv1d1 = torch.nn.Conv1d(in_channels=1, out_channels=3, kernel_size=3, groups=1, bias=True, padding=0)
        self.conv1d2 = torch.nn.Conv1d(in_channels=1, out_channels=3, kernel_size=3, groups=1, bias=True, padding=0)

    def forward(self, x1):
        x2 = self.conv1d1(x1)
        x3 = self.conv1d2(x2)
        x4 = x3 ** 2
        x5 = x4 + x2
        return x5



func = model().to('cpu')


x1 = torch.randn(1, 1, 100)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 1, 3], expected input[1, 3, 98] to have 1 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv1d of type object at 0x7ad0cd796ec0>(*(FakeTensor(..., size=(1, 3, s0 - 2)), Parameter(FakeTensor(..., size=(3, 1, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1,), (0,), (1,), 1), **{}):
Invalid channel dimensions

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 375, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 370, in _conv_forward
    return F.conv1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
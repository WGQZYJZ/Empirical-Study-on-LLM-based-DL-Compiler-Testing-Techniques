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
        self.conv1 = torch.nn.Conv2d(4, 2, 1, dilation=2, padding=2)
        self.conv2a = torch.nn.Conv2d(2, 1, 3, stride=1, padding=1)
        self.conv2b = torch.nn.Conv2d(2, 1, 1, stride=1, padding=0)

    def forward(self, x):
        v1 = self.conv1(x)
        v2a = self.conv2a(v1[:, 0:1, :, :])
        v2b = self.conv2b(v1[:, 1:2, :, :])
        v3 = torch.tanh(v2a + v2b)
        return v3



func = ModelTanh().to('cpu')


x = torch.randn(1, 4, 3, 3)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 2, 3, 3], expected input[1, 1, 7, 7] to have 2 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7db9a5996ec0>(*(FakeTensor(..., size=(1, 1, 7, 7)), Parameter(FakeTensor(..., size=(1, 2, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [1, 2, 3, 3], expected input[1, 1, 7, 7] to have 2 channels, but got 1 channels instead

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
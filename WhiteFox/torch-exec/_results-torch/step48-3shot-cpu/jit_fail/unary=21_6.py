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
        self.conv1 = torch.nn.Conv2d(16, 10, 1, dilation=2, padding=2)
        self.conv2 = torch.nn.Conv2d(10, 16, 1, dilation=2, padding=2)
        self.conv3 = torch.nn.Conv2d(16, 10, 1, dilation=2, padding=2)
        self.conv4 = torch.nn.Conv2d(10, 4, 1, dilation=2, padding=2)
        self.conv5 = torch.nn.Conv2d(4, 16, 1, dilation=2, padding=2)
        self.tanh = torch.nn.Tanh()
        self.conv6 = torch.nn.Conv2d(16, 16, 1, dilation=2, padding=2)
        self.linear = torch.nn.Linear(16, 10)
        self.softmax = torch.nn.LogSoftmax(dim=1)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        v5 = self.conv5(v4)
        v6 = self.tanh(v5)
        v7 = self.conv6(v6)
        v8 = self.linear(v7)
        v9 = self.softmax(v8)
        return v9



func = ModelTanh().to('cpu')


x = torch.randn(16, 3, 16, 16)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [10, 16, 1, 1], expected input[16, 3, 16, 16] to have 16 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x78cf8db96ec0>(*(FakeTensor(..., size=(16, 3, 16, 16)), Parameter(FakeTensor(..., size=(10, 16, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(10,), requires_grad=True)), (1, 1), (2, 2), (2, 2), 1), **{}):
Given groups=1, weight of size [10, 16, 1, 1], expected input[16, 3, 16, 16] to have 16 channels, but got 3 channels instead

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
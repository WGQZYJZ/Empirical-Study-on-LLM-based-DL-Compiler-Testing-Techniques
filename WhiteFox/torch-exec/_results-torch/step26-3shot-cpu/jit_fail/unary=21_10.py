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
        self.conv = torch.nn.Conv2d(3, 16, 3, stride=2)
        self.conv2 = torch.nn.MaxPool2d(2)
        self.conv3 = torch.nn.Conv2d(32, 64, 3)
        self.conv4 = torch.nn.AvgPool2d(2)
        self.conv5 = torch.nn.Conv2d(64, 128, 3)
        self.conv6 = torch.nn.AvgPool2d(2)

    def forward(self, x):
        v1 = torch.tanh(self.conv(x))
        v2 = self.conv2(v1)
        v3 = torch.tanh(self.conv3(v2))
        v4 = self.conv4(v3)
        v5 = torch.tanh(self.conv5(v4))
        v6 = self.conv6(v5)
        return torch.tanh(v6)



func = ModelTanh().to('cpu')


x = torch.randn(1, 3, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 32, 3, 3], expected input[1, 16, 15, 15] to have 32 channels, but got 16 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x777df9596ec0>(*(FakeTensor(..., size=(1, 16, 15, 15)), Parameter(FakeTensor(..., size=(64, 32, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [64, 32, 3, 3], expected input[1, 16, 15, 15] to have 32 channels, but got 16 channels instead

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
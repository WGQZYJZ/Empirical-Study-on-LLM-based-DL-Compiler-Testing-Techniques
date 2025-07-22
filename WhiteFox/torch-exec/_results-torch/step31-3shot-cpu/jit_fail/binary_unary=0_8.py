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
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv4 = torch.nn.Conv2d(32, 16, 7, stride=1, padding=3)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = torch.relu(v2 + x)
        v4 = self.conv3(v3)
        v5 = torch.cat([v3, v4], 1)
        v6 = self.conv4(v5)
        v7 = v4 + v6
        v8 = torch.relu(v7)
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 32, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 16, 7, 7], expected input[1, 32, 64, 64] to have 16 channels, but got 32 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x78e6ba596ec0>(*(FakeTensor(..., size=(1, 32, 64, 64)), Parameter(FakeTensor(..., size=(16, 16, 7, 7), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (1, 1), (3, 3), (1, 1), 1), **{}):
Given groups=1, weight of size [16, 16, 7, 7], expected input[1, 32, 64, 64] to have 16 channels, but got 32 channels instead

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
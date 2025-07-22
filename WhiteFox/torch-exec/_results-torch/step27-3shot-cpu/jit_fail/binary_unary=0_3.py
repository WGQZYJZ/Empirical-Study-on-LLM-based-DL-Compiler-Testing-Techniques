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
        self.conv2 = torch.nn.Conv2d(1, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, x1, x2, x3):
        v1 = self.conv1(x1)
        v2 = v1 + x2
        v3 = torch.relu(v1)
        v4 = self.conv2(v2)
        v5 = v4 + v3
        v6 = torch.relu(v5)
        v7 = self.conv3(v6)
        v8 = v7 + x3
        v9 = torch.relu(v8)
        return v9



func = Model().to('cpu')


x1 = torch.randn(16, 16, 64, 64)

x2 = torch.randn(1, 16, 64, 64)

x3 = torch.randn(16, 16, 64, 64)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 1, 7, 7], expected input[16, 16, 64, 64] to have 1 channels, but got 16 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7429a9196ec0>(*(FakeTensor(..., size=(s0, 16, 64, 64)), Parameter(FakeTensor(..., size=(16, 1, 7, 7), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (1, 1), (3, 3), (1, 1), 1), **{}):
Given groups=1, weight of size [16, 1, 7, 7], expected input[s0, 16, 64, 64] to have 1 channels, but got 16 channels instead

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
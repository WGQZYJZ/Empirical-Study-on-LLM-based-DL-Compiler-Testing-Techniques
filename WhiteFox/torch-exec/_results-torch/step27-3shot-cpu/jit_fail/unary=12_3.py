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
        self.conv = torch.nn.Conv2d(3, 24, 3, stride=2, padding=1)
        self.bn = torch.nn.BatchNorm2d(24)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = F.sigmoid(v1)
        v3 = self.bn(v2)
        v4 = self.conv(v3)
        v5 = F.sigmoid(v4)
        v6 = self.conv(v5)
        v7 = F.sigmoid(v6)
        v8 = self.conv(v7)
        v9 = F.sigmoid(v8)
        v10 = self.conv(v9)
        return v10



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [24, 3, 3, 3], expected input[1, 24, 32, 32] to have 3 channels, but got 24 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7a768a396ec0>(*(FakeTensor(..., size=(1, 24, 32, 32)), Parameter(FakeTensor(..., size=(24, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(24,), requires_grad=True)), (2, 2), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [24, 3, 3, 3], expected input[1, 24, 32, 32] to have 3 channels, but got 24 channels instead

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
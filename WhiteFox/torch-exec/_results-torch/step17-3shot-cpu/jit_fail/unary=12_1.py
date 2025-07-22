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
        self.conv = torch.nn.Conv2d(3, 3, 3, stride=1, padding=1, groups=3)
        self.conv1 = torch.nn.Conv2d(3, 8, 11, stride=2, padding=5)
        self.conv2 = torch.nn.Conv2d(128, 128, 3, stride=1, padding=1, groups=4)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv1(v1)
        v3 = torch.sigmoid(v2)
        v4 = v3 * v2
        v5 = self.conv2(v4)
        v6 = torch.sigmoid(v5)
        v7 = v6 * v4
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=4, weight of size [128, 32, 3, 3], expected input[1, 8, 32, 32] to have 128 channels, but got 8 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7e0751796ec0>(*(FakeTensor(..., size=(1, 8, 32, 32)), Parameter(FakeTensor(..., size=(128, 32, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(128,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 4), **{}):
Given groups=4, weight of size [128, 32, 3, 3], expected input[1, 8, 32, 32] to have 128 channels, but got 8 channels instead

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
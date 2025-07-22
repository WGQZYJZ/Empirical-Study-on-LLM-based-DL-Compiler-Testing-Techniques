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
        self.conv = torch.nn.Conv2d(128, 512, 1, stride=1, padding=1)
        self.conv_1 = torch.nn.Conv2d(256, 384, 1, stride=3, padding=1)
        self.conv_2 = torch.nn.Conv2d(64, 128, 1, stride=3, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.sigmoid()
        v4 = self.conv_1(v2)
        v5 = v4 * v2
        v6 = v5.tanh()
        v7 = v6.sigmoid()
        v8 = v1 * v7
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 64, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [512, 128, 1, 1], expected input[1, 64, 32, 32] to have 128 channels, but got 64 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x70e8ee996ec0>(*(FakeTensor(..., size=(1, 64, 32, 32)), Parameter(FakeTensor(..., size=(512, 128, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(512,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [512, 128, 1, 1], expected input[1, 64, 32, 32] to have 128 channels, but got 64 channels instead

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
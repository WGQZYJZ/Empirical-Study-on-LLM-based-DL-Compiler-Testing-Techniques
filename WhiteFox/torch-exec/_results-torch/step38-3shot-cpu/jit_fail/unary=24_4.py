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
        self.conv = torch.nn.Conv2d(10, 11, 5, stride=3, padding=0)

    def forward(self, x):
        negative_slope = 1
        v1 = self.conv(x)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 11, 11, 11)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [11, 10, 5, 5], expected input[1, 11, 11, 11] to have 10 channels, but got 11 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7e9cbb996ec0>(*(FakeTensor(..., size=(1, 11, 11, 11)), Parameter(FakeTensor(..., size=(11, 10, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(11,), requires_grad=True)), (3, 3), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [11, 10, 5, 5], expected input[1, 11, 11, 11] to have 10 channels, but got 11 channels instead

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
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
        self.conv1 = torch.nn.Conv2d(20, 1, 16, stride=3, padding=1, dilation=2)
        self.conv2 = torch.nn.Conv2d(1, 3, 17, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.conv2(v6)
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 20, 10, 6)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (12 x 8). Kernel size: (31 x 31). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7d4e09d96ec0>(*(FakeTensor(..., size=(1, 20, 10, 6)), Parameter(FakeTensor(..., size=(1, 20, 16, 16), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (3, 3), (1, 1), (2, 2), 1), **{}):
Calculated padded input size per channel: (12 x 8). Kernel size: (31 x 31). Kernel size can't be greater than actual input size

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
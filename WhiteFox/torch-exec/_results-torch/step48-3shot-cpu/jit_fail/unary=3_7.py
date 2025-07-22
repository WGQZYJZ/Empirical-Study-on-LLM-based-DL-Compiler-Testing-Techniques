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
        self.conv = torch.nn.Conv2d(1, 3, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(3, 6, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(3, 6, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.conv2(v6)
        v8 = v7 * 0.5
        v9 = v7 * 0.7071067811865476
        v10 = torch.erf(v9)
        v11 = v10 + 1
        v12 = v8 * v11
        v13 = self.conv3(x1)
        return v13



func = Model().to('cpu')


x1 = torch.randn(1, 1, 55, 28)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [6, 3, 1, 1], expected input[1, 1, 55, 28] to have 3 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7c4910d96ec0>(*(FakeTensor(..., size=(1, 1, s0, s1)), Parameter(FakeTensor(..., size=(6, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(6,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [6, 3, 1, 1], expected input[1, 1, s0, s1] to have 3 channels, but got 1 channels instead

from user code:
   File "<string>", line 34, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
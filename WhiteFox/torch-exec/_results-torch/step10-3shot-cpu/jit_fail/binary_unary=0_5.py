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
        self.conv = torch.nn.Conv2d(1, 1, 1, stride=1)

    def forward(self, x1, x2, x3, x4, x5, x6, x7):
        v1 = self.conv(x1)
        v2 = v1 + x2
        v3 = torch.relu(v2)
        v4 = self.conv(v3)
        v5 = v4 + x3
        v6 = torch.relu(v5)
        v7 = self.conv(x4)
        v8 = v7 + x5
        v9 = torch.relu(v8)
        v10 = self.conv(v9)
        v11 = v10 + x6
        v12 = torch.relu(v11)
        v13 = self.conv(x7)
        v14 = v13 + x8
        v15 = torch.relu(v13)
        return v15



func = Model().to('cpu')


x1 = torch.randn(1, 16, 64, 64)

x2 = torch.randn(1, 16, 64, 64)

x3 = torch.randn(1, 16, 64, 64)
x4 = 1
x5 = 1
x6 = 1
x7 = 1

test_inputs = [x1, x2, x3, x4, x5, x6, x7]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 16, 64, 64] to have 1 channels, but got 16 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7cfb17196ec0>(*(FakeTensor(..., size=(1, 16, 64, 64)), Parameter(FakeTensor(..., size=(1, 1, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [1, 1, 1, 1], expected input[1, 16, 64, 64] to have 1 channels, but got 16 channels instead

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
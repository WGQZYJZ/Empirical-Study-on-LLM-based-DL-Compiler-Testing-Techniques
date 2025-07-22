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
        self.conv = torch.nn.Conv2d(3, 1, 4, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(4, 2, 5, stride=1, padding=0)

    def forward(self, x5):
        v1 = self.conv(x5)
        v2 = v1 * 0.5
        v3 = v1 * v1
        v4 = v3 * v1
        v5 = v4 * 0.044715
        v6 = v1 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v2 * v9
        v14 = self.conv2(v10)
        v17 = v14 * 0.060631
        v19 = v17 + 1
        return v19



func = Model().to('cpu')


x5 = torch.randn(1, 3, 64, 64)

test_inputs = [x5]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 4, 5, 5], expected input[1, 1, 63, 63] to have 4 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x79fd3f396ec0>(*(FakeTensor(..., size=(1, 1, 63, 63)), Parameter(FakeTensor(..., size=(2, 4, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [2, 4, 5, 5], expected input[1, 1, 63, 63] to have 4 channels, but got 1 channels instead

from user code:
   File "<string>", line 31, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
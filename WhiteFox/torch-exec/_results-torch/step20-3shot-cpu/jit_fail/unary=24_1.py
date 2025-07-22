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

    def __init__(self, negative_slope):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = v1 > 2
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        v5 = self.conv2(x)
        v6 = v5 > 2
        v7 = v5 * self.negative_slope
        v8 = torch.where(v6, v5, v7)
        v9 = torch.cat((v4, v8), 1)
        v10 = self.conv1(v9)
        return v10


negative_slope = 0.2

func = Model(negative_slope).to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 3, 1, 1], expected input[1, 16, 66, 66] to have 3 channels, but got 16 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7fa31a196ec0>(*(FakeTensor(..., size=(1, 16, 66, 66)), Parameter(FakeTensor(..., size=(8, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [8, 3, 1, 1], expected input[1, 16, 66, 66] to have 3 channels, but got 16 channels instead

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
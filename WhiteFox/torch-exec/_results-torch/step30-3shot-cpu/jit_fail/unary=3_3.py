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
        self.conv1 = torch.nn.Conv2d(3, 1, 3, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(4, 4, 9, stride=3, padding=0)
        self.conv3 = torch.nn.Conv2d(4, 2, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v6 = self.conv2(v6)
        v7 = v6 * 0.5
        v8 = v6 * 0.7071067811865476
        v9 = torch.erf(v8)
        v10 = v9 + 1
        v11 = v7 * v10
        v12 = v11 + 1
        v13 = self.conv3(v12)
        return v13



func = Model().to('cpu')


x1 = torch.randn(1, 3, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [4, 4, 9, 9], expected input[1, 1, 30, 30] to have 4 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7b2f63f96ec0>(*(FakeTensor(..., size=(1, 1, 30, 30)), Parameter(FakeTensor(..., size=(4, 4, 9, 9), requires_grad=True)), Parameter(FakeTensor(..., size=(4,), requires_grad=True)), (3, 3), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [4, 4, 9, 9], expected input[1, 1, 30, 30] to have 4 channels, but got 1 channels instead

from user code:
   File "<string>", line 28, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
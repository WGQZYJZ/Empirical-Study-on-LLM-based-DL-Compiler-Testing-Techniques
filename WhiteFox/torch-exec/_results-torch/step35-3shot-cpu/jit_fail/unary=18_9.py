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
        self.conv = torch.nn.Conv2d(16, 24, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(16, 1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.linear(x1)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 2, 3, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [24, 16, 1, 1], expected input[1, 2, 3, 4] to have 16 channels, but got 2 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x71f763596ec0>(*(FakeTensor(..., size=(1, s0, s1, s2)), Parameter(FakeTensor(..., size=(24, 16, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(24,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [24, 16, 1, 1], expected input[1, s0, s1, s2] to have 16 channels, but got s0 channels instead

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
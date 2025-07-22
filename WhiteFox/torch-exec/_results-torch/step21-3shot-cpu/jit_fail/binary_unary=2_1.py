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
        self.conv1 = torch.nn.Conv2d(64, 32, 5, stride=2, padding=2)
        self.conv2 = torch.nn.Conv2d(32, 1, 1, stride=2, padding=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 - 0.5
        v3 = F.relu(v2)
        v4 = self.conv1(v3)
        v5 = v4 - 1.5
        v6 = F.relu(v5)
        v7 = torch.squeeze(v6, 0)
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 64, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 64, 5, 5], expected input[1, 32, 32, 32] to have 64 channels, but got 32 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x784dd9b96ec0>(*(FakeTensor(..., size=(1, 32, 32, 32)), Parameter(FakeTensor(..., size=(32, 64, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (2, 2), (2, 2), (1, 1), 1), **{}):
Given groups=1, weight of size [32, 64, 5, 5], expected input[1, 32, 32, 32] to have 64 channels, but got 32 channels instead

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
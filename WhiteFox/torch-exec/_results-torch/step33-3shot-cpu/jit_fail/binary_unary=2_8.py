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
        self.conv1 = torch.nn.Conv2d(3, 20, 5, stride=1, padding=2)
        self.conv2 = torch.nn.Conv2d(20, 50, 5, stride=1, padding=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1.transpose(-1, -2)
        v3 = v2 - 10
        v4 = F.relu(v3)
        v5 = v4.transpose(-1, -2)
        v6 = v5 + 1
        v7 = self.conv2(v6)
        v8 = v7 - 11
        v9 = F.relu(v8)
        v10 = self.conv2(v9)
        v11 = v10 + 1
        v12 = F.relu(v11)
        return v12



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [50, 20, 5, 5], expected input[1, 50, 64, 64] to have 20 channels, but got 50 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7a6a5af96ec0>(*(FakeTensor(..., size=(1, 50, s0, s1)), Parameter(FakeTensor(..., size=(50, 20, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(50,), requires_grad=True)), (1, 1), (2, 2), (1, 1), 1), **{}):
Given groups=1, weight of size [50, 20, 5, 5], expected input[1, 50, s0, s1] to have 20 channels, but got 50 channels instead

from user code:
   File "<string>", line 30, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv = torch.nn.Conv2d(3, 3, 7, stride=1, padding=3)

    def forward(self, x, y, z):
        v1 = self.conv(x)
        v2 = self.conv(v1)
        v3 = v2 + y
        v4 = torch.relu(v3)
        v5 = self.conv(v1)
        v6 = v5 + z
        return v4 + v6



func = Model().to('cpu')


x = torch.randn(1, 2, 3, 3)

y = torch.randn(1, 3, 3, 3)

z = torch.randn(1, 1, 3, 3)

test_inputs = [x, y, z]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 3, 7, 7], expected input[1, 2, 3, 3] to have 3 channels, but got 2 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7c31c7396ec0>(*(FakeTensor(..., size=(1, 2, 3, 3)), Parameter(FakeTensor(..., size=(3, 3, 7, 7), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1, 1), (3, 3), (1, 1), 1), **{}):
Given groups=1, weight of size [3, 3, 7, 7], expected input[1, 2, 3, 3] to have 3 channels, but got 2 channels instead

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
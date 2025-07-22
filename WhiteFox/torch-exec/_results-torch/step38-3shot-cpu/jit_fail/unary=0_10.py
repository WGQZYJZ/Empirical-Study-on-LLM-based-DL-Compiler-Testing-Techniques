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
        self.conv1 = torch.nn.Conv2d(26, 13, 5, stride=2, padding=1, groups=13)
        self.conv2 = torch.nn.Conv2d(6, 3, 2, stride=1, padding=0, groups=3)

    def forward(self, x6):
        v1 = self.conv1(x6)
        v2 = self.conv2(v1)
        v3 = v2 * 0.5
        v4 = v2 * v2
        v5 = v4 * v2
        v6 = v5 * 0.044715
        v7 = v2 + v6
        v8 = v7 * 0.7978845608028654
        v9 = torch.tanh(v8)
        v10 = v9 + 1
        v11 = v3 * v10
        return v11



func = Model().to('cpu')


x6 = torch.randn(1, 26, 112, 112)

test_inputs = [x6]

# JIT_FAIL
'''
direct:
Given groups=3, weight of size [3, 2, 2, 2], expected input[1, 13, 55, 55] to have 6 channels, but got 13 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7c7dc1d96ec0>(*(FakeTensor(..., size=(1, 13, 55, 55)), Parameter(FakeTensor(..., size=(3, 2, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 3), **{}):
Given groups=3, weight of size [3, 2, 2, 2], expected input[1, 13, 55, 55] to have 6 channels, but got 13 channels instead

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
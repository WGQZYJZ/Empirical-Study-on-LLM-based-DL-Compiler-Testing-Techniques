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
        self.conv = torch.nn.Conv2d(1, 8, 2, stride=2, padding=0)
        self.linear = torch.nn.Linear(8, 16)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv(v1)
        v3 = v2.flatten(start_dim=1)
        v4 = self.linear(v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 1, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 1, 2, 2], expected input[1, 8, 32, 32] to have 1 channels, but got 8 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x79efeb996ec0>(*(FakeTensor(..., size=(1, 8, (s0//2), (s1//2))), Parameter(FakeTensor(..., size=(8, 1, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), (2, 2), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [8, 1, 2, 2], expected input[1, 8, (s0//2), (s1//2)] to have 1 channels, but got 8 channels instead

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
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
        self.conv1 = torch.nn.Conv2d(36, 40, 1, stride=1, padding=0)

    def forward(self, x):
        v1 = self.conv1(x)
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 16, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [40, 36, 1, 1], expected input[1, 16, 64, 64] to have 36 channels, but got 16 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x79db0bb96ec0>(*(FakeTensor(..., size=(1, 16, 64, 64)), Parameter(FakeTensor(..., size=(40, 36, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(40,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [40, 36, 1, 1], expected input[1, 16, 64, 64] to have 36 channels, but got 16 channels instead

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
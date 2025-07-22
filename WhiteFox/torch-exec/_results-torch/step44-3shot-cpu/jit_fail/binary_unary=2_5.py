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
        self.conv1 = torch.nn.Conv2d(8, 8, 5, stride=1, padding=0)

    def forward(self, x1):
        x1 = self.conv1(x1)
        x2 = x1 - 0.75
        x3 = F.relu(x2)
        x4 = self.conv1(x3)
        x5 = x4 - 1
        x6 = F.relu(x5)
        x7 = self.conv1(x6)
        x8 = x7 + 0.25
        x9 = F.relu(x8)
        return x9



func = Model().to('cpu')


x1 = torch.randn(1, 8, 12, 12)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (4 x 4). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7c2302b96ec0>(*(FakeTensor(..., size=(1, 8, s1 - 8, s2 - 8)), Parameter(FakeTensor(..., size=(8, 8, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (s1 - 8 x s2 - 8). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
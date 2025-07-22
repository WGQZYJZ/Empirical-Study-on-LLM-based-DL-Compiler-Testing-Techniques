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
        self.conv1 = torch.nn.Conv2d(1, 1, 2)
        self.conv2 = torch.nn.Conv2d(1, 1, 2)
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x):
        x1 = self.conv1(x)
        (x1, _) = torch.min(x1, dim=3, keepdim=True)
        x2 = self.conv2(x1)
        (x2, _) = torch.max(x2, dim=2, keepdim=True)
        y = self.bn(x2)
        return y



func = Model().to('cpu')


x1 = torch.randn(1, 1, 5, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (4 x 1). Kernel size: (2 x 2). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x723d65996ec0>(*(FakeTensor(..., size=(1, 1, s0 - 1, 1)), Parameter(FakeTensor(..., size=(1, 1, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (s0 - 1 x 1). Kernel size: (2 x 2). Kernel size can't be greater than actual input size

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
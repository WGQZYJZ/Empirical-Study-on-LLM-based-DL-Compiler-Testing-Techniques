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
        self.conv = torch.nn.Conv2d(2, 1, 1)
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x1):
        x1 = self.conv(x1)
        x1 = self.bn(x1)
        x1 = self.conv(x1)
        x2 = self.conv(x1)
        x3 = self.conv(x2)
        x3 = self.conv(x3)
        x4 = self.conv(x3)
        return x4



func = Model().to('cpu')


x1 = torch.randn(1, 2, 4, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 2, 1, 1], expected input[1, 1, 4, 4] to have 2 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x70397cf96ec0>(*(FakeTensor(..., size=(1, 1, 4, 4)), Parameter(FakeTensor(..., size=(1, 2, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [1, 2, 1, 1], expected input[1, 1, 4, 4] to have 2 channels, but got 1 channels instead

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
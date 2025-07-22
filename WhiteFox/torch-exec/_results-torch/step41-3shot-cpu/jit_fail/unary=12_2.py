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
        self.conv = torch.nn.Conv2d(1, 3, 1, stride=1, padding=3)
        self.conv2d = torch.nn.Conv2d(3, 3, 1, stride=1, padding=2)
        self.conv3d = torch.nn.Conv3d(3, 3, 1, stride=1, padding=2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv2d(x1)
        v3 = self.conv3d(x1)
        return v1 + v2 + v3



func = Model().to('cpu')


x1 = torch.randn(1, 1, 4, 8)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 3, 1, 1], expected input[1, 1, 4, 8] to have 3 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x70a189996ec0>(*(FakeTensor(..., size=(1, 1, 4, 8)), Parameter(FakeTensor(..., size=(3, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1, 1), (2, 2), (1, 1), 1), **{}):
Given groups=1, weight of size [3, 3, 1, 1], expected input[1, 1, 4, 8] to have 3 channels, but got 1 channels instead

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
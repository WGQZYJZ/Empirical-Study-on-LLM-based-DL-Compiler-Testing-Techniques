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
        self.conv = torch.nn.ConvTranspose2d(1, 3, 3, padding=1, stride=2)
        self.conv1 = torch.nn.Conv2d(2, 6, 3, padding=1, stride=1)
        self.conv2 = torch.nn.ConvTranspose2d(6, 1, 7, padding=3, stride=2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = self.conv1(v2)
        v4 = torch.relu(v3)
        v5 = self.conv2(v4)
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 1, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [6, 2, 3, 3], expected input[1, 3, 447, 447] to have 2 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7fa881d96ec0>(*(FakeTensor(..., size=(1, 3, 447, 447)), Parameter(FakeTensor(..., size=(6, 2, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(6,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [6, 2, 3, 3], expected input[1, 3, 447, 447] to have 2 channels, but got 3 channels instead

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
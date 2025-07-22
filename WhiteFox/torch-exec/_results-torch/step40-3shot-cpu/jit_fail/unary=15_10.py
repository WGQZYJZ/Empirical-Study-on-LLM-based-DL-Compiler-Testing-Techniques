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
        self.conv1 = torch.nn.Conv2d(3, 64, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(64, 128, 3, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(128, 256, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v2)
        v4 = torch.relu(v1)
        v5 = self.conv3(v4)
        v6 = torch.relu(v1)
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 3, 256, 256)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [256, 128, 1, 1], expected input[1, 64, 128, 128] to have 128 channels, but got 64 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7895a0796ec0>(*(FakeTensor(..., size=(1, 64, 128, 128)), Parameter(FakeTensor(..., size=(256, 128, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(256,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [256, 128, 1, 1], expected input[1, 64, 128, 128] to have 128 channels, but got 64 channels instead

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
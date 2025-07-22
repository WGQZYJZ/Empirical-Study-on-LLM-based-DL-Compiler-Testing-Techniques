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
        self.conv = torch.nn.Conv2d(3, 8, 5, stride=2, padding=0)
        self.pool = torch.nn.MaxPool2d(kernel_size=3, stride=2, padding=0)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.relu(v1)
        v3 = self.conv(v2)
        v4 = torch.relu(v3)
        v6 = self.pool(v4)
        return v6



func = Model().to('cpu')


x = torch.randn(1, 3, 100, 100)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 3, 5, 5], expected input[1, 8, 48, 48] to have 3 channels, but got 8 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7e0a38b96ec0>(*(FakeTensor(..., size=(1, 8, 48, 48)), Parameter(FakeTensor(..., size=(8, 3, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), (2, 2), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [8, 3, 5, 5], expected input[1, 8, 48, 48] to have 3 channels, but got 8 channels instead

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
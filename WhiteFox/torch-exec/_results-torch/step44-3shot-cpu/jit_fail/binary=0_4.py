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
        self.conv1 = torch.nn.Conv2d(3, 6, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(14, 16, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 6, 3, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(16, 5, 3, stride=2, padding=1)

    def forward(self, x1, other=1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(x1)
        v4 = self.conv4(v3)
        if other == 1:
            other = torch.randn(v2.shape)
        v5 = v2 + v4 + other
        v6 = v2 + other
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 14, 3, 3], expected input[1, 6, 32, 32] to have 14 channels, but got 6 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7a0ecc996ec0>(*(FakeTensor(..., size=(1, 6, 32, 32)), Parameter(FakeTensor(..., size=(16, 14, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [16, 14, 3, 3], expected input[1, 6, 32, 32] to have 14 channels, but got 6 channels instead

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
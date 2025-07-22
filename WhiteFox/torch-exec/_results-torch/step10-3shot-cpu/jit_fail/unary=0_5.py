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
        self.conv = torch.nn.ReLU()
        self.pool = torch.nn.AvgPool2d(2, 2)
        self.conv1 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv2 = torch.nn.ReLU()
        self.conv3 = torch.nn.Conv2d(32, 16, 3, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(16, 32, 3, stride=1, padding=1)
        self.conv5 = torch.nn.ReLU()

    def forward(self, x1, x2):
        v1 = self.pool(self.conv(x1))
        v2 = self.conv2(self.conv1(v1))
        v3 = self.conv3(torch.cat((v2, x2), 1))
        v4 = self.conv4(v3)
        v5 = self.conv5(v4)
        return torch.abs(v5)



func = Model().to('cpu')


x1 = torch.randn(2, 2, 32, 32)

x2 = torch.randn(2, 3, 32, 32)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 16, 3, 3], expected input[2, 2, 16, 16] to have 16 channels, but got 2 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7979f4996ec0>(*(FakeTensor(..., size=(2, 2, 16, 16)), Parameter(FakeTensor(..., size=(16, 16, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [16, 16, 3, 3], expected input[2, 2, 16, 16] to have 16 channels, but got 2 channels instead

from user code:
   File "<string>", line 27, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.bn1 = torch.nn.BatchNorm2d(3)
        self.conv1 = torch.nn.Conv2d(3, 10, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 9, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(16, 8, 9, stride=3, padding=3)
        self.conv4 = torch.nn.Conv2d(27, 1, 11, stride=15, padding=15)
        self.bn4 = torch.nn.BatchNorm2d(27)

    def forward(self, x1):
        v1 = self.bn1(x1)
        v2 = self.conv1(v1)
        v3 = v2 * 0.5
        v4 = v2 * 0.7071067811865476
        v5 = torch.erf(v4)
        v6 = v5 + 1
        v7 = v3 * v6
        v15 = torch.tanh(v7)
        v16 = torch.sigmoid(v15)
        v8 = self.conv2(v16)
        v9 = self.conv3(v16)
        v10 = self.conv4(v16)
        v11 = v10 * 0.5
        v12 = v10 * 0.7071067811865476
        v13 = torch.erf(v12)
        v14 = v13 + 1
        return v14 * v11



func = Model().to('cpu')


x1 = torch.randn(1, 3, 56, 56)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [9, 16, 1, 1], expected input[1, 10, 56, 56] to have 16 channels, but got 10 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x76814e196ec0>(*(FakeTensor(..., size=(1, 10, 56, 56)), Parameter(FakeTensor(..., size=(9, 16, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(9,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [9, 16, 1, 1], expected input[1, 10, 56, 56] to have 16 channels, but got 10 channels instead

from user code:
   File "<string>", line 34, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
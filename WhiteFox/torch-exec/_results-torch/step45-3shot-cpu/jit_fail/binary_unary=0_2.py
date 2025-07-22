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
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv4 = torch.nn.Conv2d(32, 16, 7, stride=1, padding=3)

    def forward(self, x1, x2, x3, x4):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        v3 = v1 + x2
        v4 = torch.relu(v3)
        v5 = v2 + v4
        v6 = torch.relu(v5)
        v7 = self.conv3(v6)
        v8 = v6 + v7
        v9 = torch.relu(v8)
        v10 = self.conv4(torch.cat((v1, v9), 1))
        v11 = self.conv1(torch.cat((x3, v10), 1))
        return v11



func = Model().to('cpu')


x1 = torch.randn(1, 16, 64, 64)

x2 = torch.randn(1, 16, 64, 64)

x3 = torch.randn(1, 32, 64, 64)

x4 = torch.randn(1, 32, 64, 64)

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 16, 7, 7], expected input[1, 48, 64, 64] to have 16 channels, but got 48 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x74f147596ec0>(*(FakeTensor(..., size=(1, 48, 64, 64)), Parameter(FakeTensor(..., size=(16, 16, 7, 7), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (1, 1), (3, 3), (1, 1), 1), **{}):
Given groups=1, weight of size [16, 16, 7, 7], expected input[1, 48, 64, 64] to have 16 channels, but got 48 channels instead

from user code:
   File "<string>", line 33, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
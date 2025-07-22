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
        self.conv1 = torch.nn.Conv2d(1, 8, 16, stride=2, padding=3)
        self.conv2 = torch.nn.Conv2d(8, 4, 32, stride=2, padding=3)
        self.conv3 = torch.nn.Conv2d(4, 32, 32)

    def forward(self, x1):
        v1 = self.conv1(x1)
        r1 = F.relu(v1)
        v2 = self.conv2(r1)
        r2 = F.relu(v2)
        v3 = self.conv3(r2)
        r3 = F.relu(v3)
        v4 = r3 - 0.6
        v5 = torch.sigmoid(v4)
        v6 = r3 - 2
        v7 = v6 * v5
        v8 = torch.tanh(v5)
        v9 = torch.matmul(v7, v8)
        return v9



func = Model().to('cpu')


x1 = torch.randn(1, 1, 128, 128)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (18 x 18). Kernel size: (32 x 32). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7003caf96ec0>(*(FakeTensor(..., size=(1, 4, 18, 18)), Parameter(FakeTensor(..., size=(32, 4, 32, 32), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (18 x 18). Kernel size: (32 x 32). Kernel size can't be greater than actual input size

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
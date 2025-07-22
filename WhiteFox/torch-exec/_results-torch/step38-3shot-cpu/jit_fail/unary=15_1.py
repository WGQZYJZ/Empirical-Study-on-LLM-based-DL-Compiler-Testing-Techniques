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
        self.conv1 = torch.nn.Conv2d(3, 32, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(32, 64, 3, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(64, 128, 5, stride=2, padding=1)
        self.conv4 = torch.nn.Conv2d(128, 256, 7, stride=2, padding=1)
        self.conv5 = torch.nn.Conv2d(256, 256, 8, stride=2, padding=1)
        self.conv6 = torch.nn.Conv2d(256, 256, 9, stride=2, padding=1)
        self.conv7 = torch.nn.Conv2d(256, 256, 10, stride=2, padding=1)
        self.conv8 = torch.nn.Conv2d(256, 256, 11, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v2)
        v4 = torch.relu(v3)
        v5 = self.conv3(v4)
        v6 = torch.relu(v5)
        v7 = self.conv4(v6)
        v8 = torch.relu(v7)
        v9 = self.conv5(v8)
        v10 = torch.relu(v9)
        v11 = self.conv6(v10)
        v12 = torch.relu(v11)
        v13 = self.conv7(v12)
        v14 = torch.relu(v13)
        v15 = self.conv8(v14)
        v16 = torch.relu(v15)
        return v16



func = Model().to('cpu')


x1 = torch.randn(2, 3, 320, 320)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (8 x 8). Kernel size: (10 x 10). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7f5a63396ec0>(*(FakeTensor(..., size=(2, 256, 6, 6)), Parameter(FakeTensor(..., size=(256, 256, 10, 10), requires_grad=True)), Parameter(FakeTensor(..., size=(256,), requires_grad=True)), (2, 2), (1, 1), (1, 1), 1), **{}):
Calculated padded input size per channel: (8 x 8). Kernel size: (10 x 10). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 39, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
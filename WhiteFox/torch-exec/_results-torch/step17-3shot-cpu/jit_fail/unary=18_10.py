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
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(in_channels=16, out_channels=32, kernel_size=1, stride=2, padding=0)
        self.conv3 = torch.nn.Conv2d(in_channels=32, out_channels=4, kernel_size=1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(in_channels=4, out_channels=32, kernel_size=2, stride=2, padding=0)
        self.conv5 = torch.nn.Conv2d(in_channels=32, out_channels=8, kernel_size=1, stride=1, padding=0)
        self.conv6 = torch.nn.Conv2d(in_channels=8, out_channels=64, kernel_size=3, stride=2, padding=0)
        self.conv7 = torch.nn.Conv2d(in_channels=64, out_channels=8, kernel_size=1, stride=1, padding=0)
        self.conv8 = torch.nn.Conv2d(in_channels=8, out_channels=1, kernel_size=1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.sigmoid(v2)
        v4 = self.conv3(v3)
        v5 = self.conv4(v4)
        v6 = torch.sigmoid(v5)
        v7 = self.conv5(v6)
        v8 = self.conv6(v7)
        v9 = torch.sigmoid(v8)
        v10 = self.conv7(v9)
        v11 = self.conv8(v10)
        v12 = torch.sigmoid(v11)
        return v12



func = Model().to('cpu')


x1 = torch.randn(1, 3, 2, 3)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 2). Kernel size: (2 x 2). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7252b4796ec0>(*(FakeTensor(..., size=(1, 4, 1, 2)), Parameter(FakeTensor(..., size=(32, 4, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (2, 2), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (1 x 2). Kernel size: (2 x 2). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 31, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
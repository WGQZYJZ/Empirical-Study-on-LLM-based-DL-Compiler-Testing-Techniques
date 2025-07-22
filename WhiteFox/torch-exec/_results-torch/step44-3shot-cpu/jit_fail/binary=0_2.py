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

class MyModule(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=4, out_channels=2, kernel_size=1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(in_channels=1, out_channels=3, kernel_size=1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(in_channels=2, out_channels=4, kernel_size=1, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(in_channels=3, out_channels=4, kernel_size=1, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(in_channels=10, out_channels=4, kernel_size=1, stride=1, padding=1)

    def forward(self, x1, padding5=True, x2=True, x3=True, padding4=True, padding2=True, padding3=None):
        v1 = self.conv1(x1)
        if x2 == True:
            x2 = torch.randn(x1.shape)
        v2 = self.conv2(x2)
        if v1[0][0][0][0] == 1.0:
            v1 = torch.randn(v1.shape)
        if padding2 == True:
            padding2 = torch.randn(v2.shape)
        v3 = v1 + v2
        v4 = self.conv3(v3)
        if padding3 == None:
            padding3 = torch.randn(v4.shape)
        v5 = self.conv4(v4)
        if x3 == True:
            x3 = torch.randn(x1.shape)
        v6 = self.conv5(torch.cat((v5, x3)))
        if padding5 == True:
            padding5 = torch.randn(v6.shape)
        v7 = torch.cat((v6, padding5))
        v8 = self.conv5(torch.cat((v7, v8)))
        return v8



func = MyModule().to('cpu')


x1 = torch.randn(4, 4, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 1, 1, 1], expected input[4, 4, 32, 32] to have 1 channels, but got 4 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7a0ecc996ec0>(*(FakeTensor(..., size=(4, 4, 32, 32)), Parameter(FakeTensor(..., size=(3, 1, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [3, 1, 1, 1], expected input[4, 4, 32, 32] to have 1 channels, but got 4 channels instead

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
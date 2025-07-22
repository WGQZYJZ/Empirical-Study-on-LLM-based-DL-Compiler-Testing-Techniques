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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(8)
        self.bn2 = torch.nn.BatchNorm2d(8)
        self.bn3 = torch.nn.BatchNorm2d(3)
        self.bn4 = torch.nn.BatchNorm2d(8)
        self.conv4 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(8, 8, 5, stride=1, padding=2)
        self.conv6 = torch.nn.Conv2d(8, 8, 3, stride=1, padding=0)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.bn2(v1)
        v3 = torch.sigmoid(v2)
        v4 = self.conv2(v3)
        v5 = self.bn3(v4)
        v6 = self.relu(v5)
        v7 = self.conv3(x1)
        v8 = self.conv4(v7)
        v9 = self.bn4(v8)
        v10 = torch.sigmoid(v9)
        v11 = self.conv5(v10)
        v12 = self.conv6(v10)
        v13 = self.pad(v12)
        v14 = self.conv3(v13)
        v17 = self.conv5(v14)
        v15 = self.bn4(v17)
        v18 = torch.sigmoid(v15)
        v19 = self.conv6(v18)
        v26 = torch.conv2d(x1, self.weight, self.bias, self.stride, self.padding, self.dilation, self.groups)
        v20 = self.bn4(v26)
        v21 = torch.sigmoid(v20)
        return v21



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3, 64, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 3, 1, 1], expected input[1, 8, 66, 66] to have 3 channels, but got 8 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x732d05596ec0>(*(FakeTensor(..., size=(1, 8, 66, 66)), Parameter(FakeTensor(..., size=(3, 3, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [3, 3, 1, 1], expected input[1, 8, 66, 66] to have 3 channels, but got 8 channels instead

from user code:
   File "<string>", line 32, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
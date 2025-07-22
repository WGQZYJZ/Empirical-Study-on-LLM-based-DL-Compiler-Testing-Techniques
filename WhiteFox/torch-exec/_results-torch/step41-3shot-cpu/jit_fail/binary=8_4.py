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
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(3, 32, 3, stride=2, padding=1)
        self.conv6 = torch.nn.Conv2d(32, 32, 3, stride=2, padding=1)
        self.conv7 = torch.nn.Conv2d(64, 32, 3, stride=2, padding=1)
        self.conv8 = torch.nn.Conv2d(64, 32, 3, stride=2, padding=1)
        self.conv9 = torch.nn.Conv2d(128, 32, 3, stride=2, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        v3 = self.conv3(x2)
        v4 = self.conv4(x2)
        v5 = torch.cat((v1, v2, v3, v4), dim=1)
        v6 = self.conv5(v5)
        v7 = self.conv6(v5)
        v8 = torch.cat((v6, v7), dim=1)
        v9 = self.conv7(v8)
        v10 = self.conv8(v8)
        v11 = torch.cat((v9, v10), dim=1)
        v12 = self.conv9(v11)
        return v12



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3, 64, 64)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 3, 3, 3], expected input[1, 32, 66, 66] to have 3 channels, but got 32 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7725e3f96ec0>(*(FakeTensor(..., size=(1, 32, 66, 66)), Parameter(FakeTensor(..., size=(32, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (2, 2), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [32, 3, 3, 3], expected input[1, 32, 66, 66] to have 3 channels, but got 32 channels instead

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
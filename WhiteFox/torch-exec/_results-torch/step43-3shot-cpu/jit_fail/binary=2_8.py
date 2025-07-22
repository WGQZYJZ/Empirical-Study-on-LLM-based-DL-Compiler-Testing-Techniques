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
        self.conv = torch.nn.Conv2d(64, 128, 16, stride=16, padding=16)
        self.relu1 = torch.nn.ReLU(inplace=False)
        self.conv1 = torch.nn.Conv2d(128, 64, 1, stride=1, padding=0)
        self.relu2 = torch.nn.ReLU(inplace=False)
        self.conv2 = torch.nn.Conv2d(64, 32, 1, stride=1, padding=0)
        self.relu3 = torch.nn.ReLU(inplace=False)
        self.conv3 = torch.nn.Conv2d(32, 16, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.relu1(self.conv(x1))
        v2 = self.relu2(self.conv1(v1))
        v3 = self.conv2(v2)
        v4 = self.relu3(self.conv3(v3))
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 3, 128, 128)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [128, 64, 16, 16], expected input[1, 3, 128, 128] to have 64 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x79195dd96ec0>(*(FakeTensor(..., size=(1, 3, 128, 128)), Parameter(FakeTensor(..., size=(128, 64, 16, 16), requires_grad=True)), Parameter(FakeTensor(..., size=(128,), requires_grad=True)), (16, 16), (16, 16), (1, 1), 1), **{}):
Given groups=1, weight of size [128, 64, 16, 16], expected input[1, 3, 128, 128] to have 64 channels, but got 3 channels instead

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
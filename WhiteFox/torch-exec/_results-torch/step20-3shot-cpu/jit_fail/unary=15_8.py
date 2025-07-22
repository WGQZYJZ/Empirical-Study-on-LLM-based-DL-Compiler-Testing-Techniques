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
        self.conv1 = torch.nn.Conv2d(3, 32, 5, stride=1, padding=2, bias=False)
        self.relu1 = torch.nn.ReLU6()
        self.conv2 = torch.nn.Conv2d(32, 3, 1, stride=1, padding=0, bias=False)
        self.relu2 = torch.nn.ReLU6()
        self.conv3 = torch.nn.Conv2d(32, 1, 1, stride=1, padding=0)
        self.relu3 = torch.nn.ReLU6()
        self.conv4 = torch.nn.Conv2d(1, 32, 5, stride=1, padding=2, bias=False)
        self.relu4 = torch.nn.ReLU6()
        self.conv5 = torch.nn.Conv2d(32, 3, 1, stride=1, padding=0, bias=False)
        self.relu5 = torch.nn.ReLU6()
        self.conv6 = torch.nn.Conv2d(32, 3, 1, stride=1, padding=0)
        self.relu6 = torch.nn.ReLU6()

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.relu1(v1)
        v3 = self.conv2(v2)
        v4 = self.relu2(v3)
        v5 = self.conv3(v4)
        v6 = self.relu3(v5)
        v7 = self.conv4(v6)
        v8 = self.relu4(v7)
        v9 = self.conv5(v8)
        v10 = self.relu5(v9)
        v11 = self.conv6(v10)
        v12 = self.relu6(v11)
        return v12



func = Model().to('cpu')


x1 = torch.randn(4, 3, 320, 320)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 32, 1, 1], expected input[4, 3, 320, 320] to have 32 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7f1a10196ec0>(*(FakeTensor(..., size=(4, 3, 320, 320)), Parameter(FakeTensor(..., size=(1, 32, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [1, 32, 1, 1], expected input[4, 3, 320, 320] to have 32 channels, but got 3 channels instead

from user code:
   File "<string>", line 35, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
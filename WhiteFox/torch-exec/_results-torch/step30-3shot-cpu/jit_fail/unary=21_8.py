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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super(ModelTanh, self).__init__()
        self.conv_1 = torch.nn.Conv2d(128, 128, 3)
        self.conv_2 = torch.nn.Conv2d(128, 1, 1)
        self.conv_3 = torch.nn.Conv2d(128, 128, 3)
        self.conv_4 = torch.nn.Conv2d(128, 128, 3, padding=1)
        self.conv_5 = torch.nn.Conv2d(128, 128, 3)

    def forward(self, x1):
        x2 = self.conv_1(x1)
        x2 = torch.tanh(x2)
        x3 = self.conv_2(x2)
        x4 = self.conv_3(x3)
        x5 = self.conv_4(x4)
        x6 = self.conv_5(x4)
        x4 = torch.tanh(x5 + x6)
        x4 = x4 + x1
        return x4



func = ModelTanh().to('cpu')


x1 = torch.randn(1, 128, 16, 16)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [128, 128, 3, 3], expected input[1, 1, 14, 14] to have 128 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x740599596ec0>(*(FakeTensor(..., size=(1, 1, 14, 14)), Parameter(FakeTensor(..., size=(128, 128, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(128,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [128, 128, 3, 3], expected input[1, 1, 14, 14] to have 128 channels, but got 1 channels instead

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
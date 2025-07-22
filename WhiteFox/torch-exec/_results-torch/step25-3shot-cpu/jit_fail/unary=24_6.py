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

class ConvModule(torch.nn.Module):

    def __init__(self, channels, kernel_size):
        super().__init__()
        self.padding = kernel_size // 2
        self.conv = torch.nn.Conv2d(channels, channels, kernel_size)
        self.bn = torch.nn.BatchNorm2d(channels)

    def forward(self, x):
        x = torch.nn.functional.pad(x, [0, 0, 0, 0, self.padding, self.padding, self.padding, self.padding])
        x = self.conv(x)
        x = self.bn(x)
        x = torch.nn.functional.leaky_relu(x, negative_slope=0.1)
        return x

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        x = ConvModule(12, 3)(x)
        return (x, 0)



func = Model().to('cpu')


x1 = torch.randn(1, 12, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [12, 12, 3, 3], expected input[3, 14, 32, 32] to have 12 channels, but got 14 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x78d54cd96ec0>(*(FakeTensor(..., size=(3, 14, 32, 32)), Parameter(FakeTensor(..., size=(12, 12, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(12,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [12, 12, 3, 3], expected input[3, 14, 32, 32] to have 12 channels, but got 14 channels instead

from user code:
   File "<string>", line 34, in torch_dynamo_resume_in_forward_at_34
  File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
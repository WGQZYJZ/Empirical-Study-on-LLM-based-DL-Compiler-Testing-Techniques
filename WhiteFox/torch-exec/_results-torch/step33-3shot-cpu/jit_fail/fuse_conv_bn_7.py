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
        self.conv1 = torch.nn.Conv2d(3, 64, 7)
        self.pad = torch.nn.ConstantPad2d((3, 3, 2, 2), 2.0)
        self.conv2 = torch.nn.Conv2d(64, 128, 6)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x3):
        y = self.conv1(x3)
        z = self.pad(x3)
        w = self.conv2(z)
        v = self.pad(y)
        u = self.conv1(v)
        a = self.bn(u)
        b = torch.tanh(a)
        return (a, b, y, z, v, w)



func = Model().to('cpu')


x3 = torch.randn(1, 3, 10, 10)

test_inputs = [x3]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [128, 64, 6, 6], expected input[1, 3, 14, 16] to have 64 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x73d6f4796ec0>(*(FakeTensor(..., size=(1, 3, s0 + 4, s1 + 6)), Parameter(FakeTensor(..., size=(128, 64, 6, 6), requires_grad=True)), Parameter(FakeTensor(..., size=(128,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [128, 64, 6, 6], expected input[1, 3, s0 + 4, s1 + 6] to have 64 channels, but got 3 channels instead

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv = torch.nn.Conv2d(5, 4, 1, stride=1, bias=False)

    def forward(self, x1, x2=torch.randn((1, 2, 16, 16)), x3=1, x4=5, padding1=None, padding2=None, padding3=None, padding4=None, x5=None):
        x1 = self.conv(x1)
        v1 = x4
        v3 = self.conv(x3)
        v4 = x1
        v2 = v3 + v4
        return v2



func = Model().to('cpu')


x3 = torch.randn(1, 3, 16, 16)

x4 = torch.randn(1, 4, 16, 16)

x5 = torch.zeros((1, 3, 16, 16))
x1 = 1

test_inputs = [x3, x4, x5, x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [4, 5, 1, 1], expected input[1, 3, 16, 16] to have 5 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x781904796ec0>(*(FakeTensor(..., size=(1, s0, s1, s2)), Parameter(FakeTensor(..., size=(4, 5, 1, 1), requires_grad=True)), None, (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [4, 5, 1, 1], expected input[1, s0, s1, s2] to have 5 channels, but got s0 channels instead

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
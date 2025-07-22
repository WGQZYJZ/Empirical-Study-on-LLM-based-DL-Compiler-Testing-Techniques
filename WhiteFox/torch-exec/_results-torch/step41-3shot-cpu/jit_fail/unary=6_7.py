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
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1, groups=3)

    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = 3 + t1
        t3 = torch.clamp(t2, 0, 6)
        t4 = t1 * t3
        t5 = t4 / 6
        return t5



func = Model().to('cpu')


x1 = torch.randn(1, 6, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=3, weight of size [3, 1, 1, 1], expected input[1, 6, 64, 64] to have 3 channels, but got 6 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7f2470196ec0>(*(FakeTensor(..., size=(1, s0, 64, 64)), Parameter(FakeTensor(..., size=(3, 1, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 3), **{}):
Given groups=3, weight of size [3, 1, 1, 1], expected input[1, s0, 64, 64] to have 3 channels, but got s0 channels instead

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
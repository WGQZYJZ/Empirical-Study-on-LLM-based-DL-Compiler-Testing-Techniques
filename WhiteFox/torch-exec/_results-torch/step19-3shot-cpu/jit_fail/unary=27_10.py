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

    def __init__(self, min=-6.0, max=-6.0):
        super().__init__()
        self.t = torch.nn.Conv2d(4, 32, 5, stride=1, padding=2)
        self.min = min
        self.max = max

    def forward(self, x1):
        t1 = self.t(x1)
        t2 = torch.clamp_min(t1, self.min)
        t3 = torch.clamp_max(t2, self.max)
        return t3



func = Model().to('cpu')


x1 = torch.randn(1, 16, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 4, 5, 5], expected input[1, 16, 32, 32] to have 4 channels, but got 16 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x79f1cf396ec0>(*(FakeTensor(..., size=(1, s0, s1, s2)), Parameter(FakeTensor(..., size=(32, 4, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (1, 1), (2, 2), (1, 1), 1), **{}):
Given groups=1, weight of size [32, 4, 5, 5], expected input[1, s0, s1, s2] to have 4 channels, but got s0 channels instead

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
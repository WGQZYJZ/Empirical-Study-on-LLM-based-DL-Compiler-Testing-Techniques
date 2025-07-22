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
        self.conv = torch.nn.Conv2d(64, 64, 1, stride=1, padding=1)

    def forward(self, x1, other=1, padding1=None, padding2=None, padding3=None, padding4=None):
        v1 = self.conv(x1)
        if padding1 == None:
            padding1 = torch.randn(v1.shape)
        v2 = v1 + other
        v3 = torch.cat([v2, padding1])
        v4 = torch.cat([v3, padding2])
        v5 = torch.cat([v4, padding3])
        v6 = torch.cat([v5, padding4])
        return v6



func = Model().to('cpu')


x1 = torch.randn(3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 64, 1, 1], expected input[1, 3, 64, 64] to have 64 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x749615996ec0>(*(FakeTensor(..., size=(s0, s1, s2)), Parameter(FakeTensor(..., size=(64, 64, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [64, 64, 1, 1], expected input[1, s0, s1, s2] to have 64 channels, but got s0 channels instead

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
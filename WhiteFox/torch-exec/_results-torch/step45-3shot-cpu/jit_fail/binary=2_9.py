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
        self.conv = torch.nn.Conv2d(4, 64, 5, stride=3, padding=0, dilation=1, groups=1, bias=False)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 - 0
        return v2



func = Model().to('cpu')


x = torch.randn(1, 8, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 4, 5, 5], expected input[1, 8, 64, 64] to have 4 channels, but got 8 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x75910ab96ec0>(*(FakeTensor(..., size=(1, s0, s1, s2)), Parameter(FakeTensor(..., size=(64, 4, 5, 5), requires_grad=True)), None, (3, 3), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [64, 4, 5, 5], expected input[1, s0, s1, s2] to have 4 channels, but got s0 channels instead

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
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
        self.conv = torch.nn.Conv2d(8, 12, 3, stride=1, padding=1)

    def forward(self, x1, other, padding1=None, padding2=None, padding3=None, padding4=None, padding5=None):
        v1 = self.conv(x1)
        t1 = v1 + other
        return t1



func = Model().to('cpu')


x1 = torch.randn(2, 50, 64, 64)
other = 1

test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [12, 8, 3, 3], expected input[2, 50, 64, 64] to have 8 channels, but got 50 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7cd20dd96ec0>(*(FakeTensor(..., size=(s0, s1, s2, s3)), Parameter(FakeTensor(..., size=(12, 8, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(12,), requires_grad=True)), (1, 1), (1, 1), (1, 1), 1), **{}):
Given groups=1, weight of size [12, 8, 3, 3], expected input[s0, s1, s2, s3] to have 8 channels, but got s1 channels instead

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
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

    def __init__(self, min_value=-1.7):
        super().__init__()
        self.conv = torch.nn.Conv1d(9, 2, 1, stride=3)
        self.min_value = min_value

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        return v2



func = Model().to('cpu')


x1 = torch.randn(750, 9)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 9, 1], expected input[1, 750, 9] to have 9 channels, but got 750 channels instead

jit:
Failed running call_function <built-in method conv1d of type object at 0x70944d796ec0>(*(FakeTensor(..., size=(s0, s1)), Parameter(FakeTensor(..., size=(2, 9, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), (3,), (0,), (1,), 1), **{}):
Invalid channel dimensions

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 375, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 370, in _conv_forward
    return F.conv1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
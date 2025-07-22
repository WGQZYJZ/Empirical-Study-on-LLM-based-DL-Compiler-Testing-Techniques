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
        super().__init__()
        self.conv = torch.nn.Conv2d(4, 11, 6, dilation=2)

    def forward(self, x0):
        v1 = self.conv(x0)
        v2 = torch.tanh(v1)
        return v2



func = ModelTanh().to('cpu')


x0 = torch.randn(1, 4, 1, 1)

test_inputs = [x0]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 1). Kernel size: (11 x 11). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x783b08596ec0>(*(FakeTensor(..., size=(1, 4, 1, 1)), Parameter(FakeTensor(..., size=(11, 4, 6, 6), requires_grad=True)), Parameter(FakeTensor(..., size=(11,), requires_grad=True)), (1, 1), (0, 0), (2, 2), 1), **{}):
Calculated padded input size per channel: (1 x 1). Kernel size: (11 x 11). Kernel size can't be greater than actual input size

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
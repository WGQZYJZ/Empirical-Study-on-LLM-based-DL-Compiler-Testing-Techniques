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
        self.conv = torch.nn.Conv2d(1, 1, (1,), 1, 0, bias=True)
        self.tanh = torch.nn.Tanh()

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.tanh(v1)
        b1 = 3 ** 4
        b2 = len(set(str(x))) - x.size(0)
        v3 = v2 * b1 + b2
        v4 = v3 / v3
        return v4



func = ModelTanh().to('cpu')


x = torch.randn(238, 1, 15, 26)

test_inputs = [x]

# JIT_FAIL
'''
direct:
expected stride to be a single integer value or a list of 1 values to match the convolution dimensions, but got stride=[1, 1]

jit:
Failed running call_function <built-in method conv2d of type object at 0x7019a4b96ec0>(*(FakeTensor(..., size=(s0, 1, s1, s2)), Parameter(FakeTensor(..., size=(1, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
tuple index out of range

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
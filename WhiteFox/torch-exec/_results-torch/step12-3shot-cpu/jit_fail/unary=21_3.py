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

class conv2d_tanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 1, (1,), (1,), 0)

    def forward(self, x):
        tanh = torch.tanh(self.conv(x))
        return tanh

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.m1 = conv2d_tanh()

    def forward(self, x):
        v1 = self.m1(x)
        v2 = torch.tanh(v1)
        return v2



func = ModelTanh().to('cpu')


tensor = torch.randn((1, 3, 128, 128))

test_inputs = [tensor]

# JIT_FAIL
'''
direct:
expected padding to be a single integer value or a list of 1 values to match the convolution dimensions, but got padding=[0, 0]

jit:
Failed running call_function <built-in method conv2d of type object at 0x703513996ec0>(*(FakeTensor(..., size=(1, 3, 128, 128)), Parameter(FakeTensor(..., size=(1, 3, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1,), (0, 0), (1, 1), 1), **{}):
tuple index out of range

from user code:
   File "<string>", line 30, in forward
  File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
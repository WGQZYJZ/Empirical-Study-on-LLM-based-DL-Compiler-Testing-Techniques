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
        self.conv = torch.nn.Conv2d(3, 11, 20, stride=2, padding=10, dilation=20)
        self.tanh = torch.nn.Tanh()

    def forward(self, x2):
        v1 = self.conv(x2)
        v2 = self.tanh(v1)
        return v2



func = ModelTanh().to('cpu')


x2 = torch.randn(1, 3, 224, 224)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (244 x 244). Kernel size: (381 x 381). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x71fce6996ec0>(*(FakeTensor(..., size=(1, 3, 224, 224)), Parameter(FakeTensor(..., size=(11, 3, 20, 20), requires_grad=True)), Parameter(FakeTensor(..., size=(11,), requires_grad=True)), (2, 2), (10, 10), (20, 20), 1), **{}):
Calculated padded input size per channel: (244 x 244). Kernel size: (381 x 381). Kernel size can't be greater than actual input size

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
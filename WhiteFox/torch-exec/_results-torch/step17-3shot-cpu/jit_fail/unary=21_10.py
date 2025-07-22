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
        self.conv = torch.nn.Conv2d(1, 2, 3, stride=1)
        self.conv2 = torch.nn.Conv2d(21, 12, 7, padding=13)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.conv2(v1)
        return torch.tanh(v2)



func = ModelTanh().to('cpu')


x = torch.randn(1, 1, 3, 7)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [12, 21, 7, 7], expected input[1, 2, 1, 5] to have 21 channels, but got 2 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7ff396b96ec0>(*(FakeTensor(..., size=(1, 2, 1, 5)), Parameter(FakeTensor(..., size=(12, 21, 7, 7), requires_grad=True)), Parameter(FakeTensor(..., size=(12,), requires_grad=True)), (1, 1), (13, 13), (1, 1), 1), **{}):
Given groups=1, weight of size [12, 21, 7, 7], expected input[1, 2, 1, 5] to have 21 channels, but got 2 channels instead

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
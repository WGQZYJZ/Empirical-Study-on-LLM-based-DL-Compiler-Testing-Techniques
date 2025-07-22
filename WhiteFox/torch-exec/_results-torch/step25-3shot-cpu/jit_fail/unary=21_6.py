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
        self.conv1 = torch.nn.Conv2d(1, 1, 15, stride=2)
        self.conv2 = torch.nn.Conv2d(1, 1, 8, stride=3, padding=15)

    def forward(self, x):
        x = self.conv2(self.conv1(x))
        x = torch.tanh(x)
        return x



func = ModelTanh().to('cpu')


x = torch.randn(5, 5, 5, 5)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 15, 15], expected input[5, 5, 5, 5] to have 1 channels, but got 5 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x7c9244396ec0>(*(FakeTensor(..., size=(s0, s1, s2, s3)), Parameter(FakeTensor(..., size=(1, 1, 15, 15), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (2, 2), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [1, 1, 15, 15], expected input[s0, s1, s2, s3] to have 1 channels, but got s1 channels instead

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
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
        self.conv1 = torch.nn.Conv2d(16, 16, 3, stride=16, padding=15)

    def forward(self, input):
        v1 = torch.relu(self.conv1(input))
        v2 = torch.tanh(v1)
        v3 = torch.matmul(v2, v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 8, 28, 28)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [16, 16, 3, 3], expected input[1, 8, 28, 28] to have 16 channels, but got 8 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x754058396ec0>(*(FakeTensor(..., size=(1, 8, 28, 28)), Parameter(FakeTensor(..., size=(16, 16, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(16,), requires_grad=True)), (16, 16), (15, 15), (1, 1), 1), **{}):
Given groups=1, weight of size [16, 16, 3, 3], expected input[1, 8, 28, 28] to have 16 channels, but got 8 channels instead

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
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
        self.conv1 = torch.nn.Conv2d(3, 32, 3, stride=1, padding=0)

    def forward(self, x1, x2):
        v1 = torch.cat((x1, x2), 1)
        v2 = self.conv1(v1)
        v3 = v2 - 203
        v4 = F.relu(v3)
        t = torch.zeros_like(x1)
        return t



func = Model().to('cpu')


x1 = torch.randn(1, 3, 16, 16)

x2 = torch.randn(1, 23, 16, 16)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 3, 3, 3], expected input[1, 26, 16, 16] to have 3 channels, but got 26 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x76f1b7596ec0>(*(FakeTensor(..., size=(1, 26, 16, 16)), Parameter(FakeTensor(..., size=(32, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [32, 3, 3, 3], expected input[1, 26, 16, 16] to have 3 channels, but got 26 channels instead

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
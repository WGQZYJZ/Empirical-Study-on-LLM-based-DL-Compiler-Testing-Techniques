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
        self.conv2 = torch.nn.Conv2d(16, 2, 7, stride=1, padding=3)
        self.conv1 = torch.nn.Conv2d(16, 2, 3, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        return v2



func = Model().to('cpu')


x = torch.randn(1, 16, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 16, 7, 7], expected input[1, 2, 64, 64] to have 16 channels, but got 2 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x77e58df96ec0>(*(FakeTensor(..., size=(1, 2, 64, 64)), Parameter(FakeTensor(..., size=(2, 16, 7, 7), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), (1, 1), (3, 3), (1, 1), 1), **{}):
Given groups=1, weight of size [2, 16, 7, 7], expected input[1, 2, 64, 64] to have 16 channels, but got 2 channels instead

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
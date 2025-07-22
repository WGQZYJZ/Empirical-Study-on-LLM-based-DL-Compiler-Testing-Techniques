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
        self.conv1 = torch.nn.Conv2d(2, 8, 7)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.layer_wrapper(v1)
        return v2

    def layer_wrapper(self, x):
        v3 = self.conv1(x)
        return v3



func = Model().to('cpu')


x = torch.randn(1, 2, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [8, 2, 7, 7], expected input[1, 8, 58, 58] to have 2 channels, but got 8 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x765cc9b96ec0>(*(FakeTensor(..., size=(1, 8, 58, 58)), Parameter(FakeTensor(..., size=(8, 2, 7, 7), requires_grad=True)), Parameter(FakeTensor(..., size=(8,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [8, 2, 7, 7], expected input[1, 8, 58, 58] to have 2 channels, but got 8 channels instead

from user code:
   File "<string>", line 21, in forward
  File "<string>", line 25, in layer_wrapper
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
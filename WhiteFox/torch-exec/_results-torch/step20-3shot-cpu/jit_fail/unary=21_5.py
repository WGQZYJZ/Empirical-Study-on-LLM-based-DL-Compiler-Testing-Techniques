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
        self.conv = torch.nn.Conv2d(6, 3, (16, 16), stride=(16, 16), bias=False)

    def forward(self, x0):
        v1 = self.conv(x0)
        v2 = torch.tanh(v1)
        return v2



func = ModelTanh().to('cpu')


x0 = torch.randn(1, 1, 32, 32)

test_inputs = [x0]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [3, 6, 16, 16], expected input[1, 1, 32, 32] to have 6 channels, but got 1 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x77ef6ed96ec0>(*(FakeTensor(..., size=(1, 1, 32, 32)), Parameter(FakeTensor(..., size=(3, 6, 16, 16), requires_grad=True)), None, (16, 16), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [3, 6, 16, 16], expected input[1, 1, 32, 32] to have 6 channels, but got 1 channels instead

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
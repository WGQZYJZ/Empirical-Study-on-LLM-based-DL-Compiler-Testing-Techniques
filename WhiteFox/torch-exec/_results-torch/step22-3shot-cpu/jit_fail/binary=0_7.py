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
        self.conv = torch.nn.Conv3d(64, 64, 1, stride=1, padding=1)

    def forward(self, x, other1=1, padding=None):
        v1 = self.conv(x)
        if padding == None:
            padding = torch.randn(x.shape)
        v = v1 + other1
        return v



func = Model().to('cpu')


x1 = torch.randn(1, 8, 32, 32, 32)
x = 1

test_inputs = [x1, x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [64, 64, 1, 1, 1], expected input[1, 8, 32, 32, 32] to have 64 channels, but got 8 channels instead

jit:
Failed running call_function <built-in method conv3d of type object at 0x7479b0796ec0>(*(FakeTensor(..., size=(1, 8, 32, 32, 32)), Parameter(FakeTensor(..., size=(64, 64, 1, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True)), (1, 1, 1), (1, 1, 1), (1, 1, 1), 1), **{}):
Given groups=1, weight of size [64, 64, 1, 1, 1], expected input[1, 8, 32, 32, 32] to have 64 channels, but got 8 channels instead

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 725, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 720, in _conv_forward
    return F.conv3d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
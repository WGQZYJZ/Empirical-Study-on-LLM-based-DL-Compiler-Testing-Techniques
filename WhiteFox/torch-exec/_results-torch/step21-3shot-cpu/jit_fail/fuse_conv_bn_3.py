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
        self.conv = torch.nn.Conv1d(2, 4, 3, groups=2)
        c = torch.nn.Conv1d(1, 2, 1)
        bn = torch.nn.BatchNorm1d(2)
        self.layer = torch.nn.Sequential(bn, c)

    def forward(self, x1):
        x1 = self.layer(x1)
        v1 = self.conv(x1)
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 2, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [2, 1, 1], expected input[1, 2, 4] to have 1 channels, but got 2 channels instead

jit:
Failed running call_function <built-in method conv1d of type object at 0x70397cf96ec0>(*(FakeTensor(..., size=(1, 2, 4)), Parameter(FakeTensor(..., size=(2, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(2,), requires_grad=True)), (1,), (0,), (1,), 1), **{}):
Invalid channel dimensions

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 375, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 370, in _conv_forward
    return F.conv1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
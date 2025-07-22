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

    def __init__(self, x: int):
        super().__init__()
        self.conv1 = torch.nn.Conv1d(1, x, 1)
        self.conv2 = torch.nn.Conv1d(1, x, 1)

    def forward(self, x1: torch.Tensor) -> torch.Tensor:
        v1 = self.conv1(x1)
        v2 = torch.clamp(v1, min=1000, max=10000)
        v3 = self.conv2(v2)
        v4 = torch.relu(v3).reshape([1, x])
        v5 = torch.softmax(v4, -1)
        return v5


x = 10

func = Model(x).to('cpu')


x1 = torch.randn(1, 1, 100)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [10, 1, 1], expected input[1, 10, 100] to have 1 channels, but got 10 channels instead

jit:
Failed running call_function <built-in method conv1d of type object at 0x7895a0796ec0>(*(FakeTensor(..., size=(1, 10, s0)), Parameter(FakeTensor(..., size=(10, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(10,), requires_grad=True)), (1,), (0,), (1,), 1), **{}):
Invalid channel dimensions

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 375, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 370, in _conv_forward
    return F.conv1d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
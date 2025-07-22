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

    def __init__(self, inp, mid, out):
        super().__init__()
        torch.manual_seed(1)
        self.conv1 = nn.Conv2d(inp, mid, kernel_size=3)
        torch.manual_seed(1)
        self.bn = nn.BatchNorm1d(mid)
        torch.manual_seed(1)
        self.conv2 = nn.Conv1d(mid, out, kernel_size=3)

    def forward(self, x):
        x1 = self.conv1(x)
        x1 = self.bn(x1)
        x2 = self.conv1(x)
        x2 = self.conv2(x)
        x = x1 + x2
        return x


inp = 1
mid = 1
out = 1

func = Model(inp, mid, out).to('cpu')


x = torch.randn(1, 4, 5, 5)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [1, 1, 3, 3], expected input[1, 4, 5, 5] to have 1 channels, but got 4 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x767573996ec0>(*(FakeTensor(..., size=(1, 4, 5, 5)), Parameter(FakeTensor(..., size=(1, 1, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [1, 1, 3, 3], expected input[1, 4, 5, 5] to have 1 channels, but got 4 channels instead

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
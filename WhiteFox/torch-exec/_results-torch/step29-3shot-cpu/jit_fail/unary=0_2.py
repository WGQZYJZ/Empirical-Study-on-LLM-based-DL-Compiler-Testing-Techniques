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
        self.conv1 = torch.nn.Conv2d(1, 3, 32, stride=4, padding=4)
        self.conv2 = torch.nn.Conv2d(3, 3, 32, stride=2, padding=1)

    def forward(self, x4):
        v1 = self.conv1(x4)
        v2 = self.conv2(v1)
        v3 = v2 * 0.5
        v4 = v2 * v2
        v5 = v4 * v2
        v6 = v5 * 0.044715
        v7 = v2 + v6
        v8 = v7 * 0.7978845608028654
        v9 = torch.tanh(v8)
        v10 = v9 + 1
        v11 = v3 * v10
        return v11



func = Model().to('cpu')


x4 = torch.randn(1, 1, 64, 64)

test_inputs = [x4]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (13 x 13). Kernel size: (32 x 32). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x76f8efd96ec0>(*(FakeTensor(..., size=(1, 3, ((s0//4)) - 5, ((s1//4)) - 5)), Parameter(FakeTensor(..., size=(3, 3, 32, 32), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (2, 2), (1, 1), (1, 1), 1), **{}):
Calculated padded input size per channel: (((s0//4)) - 3 x ((s1//4)) - 3). Kernel size: (32 x 32). Kernel size can't be greater than actual input size

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
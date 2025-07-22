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
        self.conv = torch.nn.Conv2d(20, 256, 6, stride=6)

    def forward(self, x3):
        v1 = self.conv(x3)
        v2 = v1 * 0.5
        v3 = v1 * v1
        v4 = v3 * v1
        v5 = v4 * 0.044715
        v6 = v1 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v2 * v9
        return v10



func = Model().to('cpu')


x3 = torch.randn(1, 20, 64, 4)

test_inputs = [x3]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (64 x 4). Kernel size: (6 x 6). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x76c575596ec0>(*(FakeTensor(..., size=(1, 20, s1, s2)), Parameter(FakeTensor(..., size=(256, 20, 6, 6), requires_grad=True)), Parameter(FakeTensor(..., size=(256,), requires_grad=True)), (6, 6), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (s1 x s2). Kernel size: (6 x 6). Kernel size can't be greater than actual input size

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
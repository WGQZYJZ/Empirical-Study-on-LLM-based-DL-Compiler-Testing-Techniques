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
        self.conv = torch.nn.Conv2d(11, 9, 5, stride=3, padding=0)
        self.bn = torch.nn.BatchNorm2d(9)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.flatten(v1)
        v3 = torch.flatten(v2)
        v4 = v3 * 0.5
        v5 = v3 * v3
        v6 = v5 * v3
        v7 = v6 * 0.044715
        v8 = v3 + v7
        v9 = v8 * 0.7978845608028654
        v10 = torch.tanh(v9)
        v11 = v10 + 1
        v12 = v4 * v11
        return v12



func = Model().to('cpu')


x1 = torch.randn(1, 11, 6329, 1)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (6329 x 1). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7893a1d96ec0>(*(FakeTensor(..., size=(1, 11, 6329, 1)), Parameter(FakeTensor(..., size=(9, 11, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(9,), requires_grad=True)), (3, 3), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (6329 x 1). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

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
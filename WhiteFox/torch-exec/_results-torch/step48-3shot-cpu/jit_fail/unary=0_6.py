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
        self.conv = torch.nn.Conv2d(1, 14, 512, stride=2, padding=1)

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


x3 = torch.randn(1, 1, 256, 256)

test_inputs = [x3]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (258 x 258). Kernel size: (512 x 512). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7d9ca7196ec0>(*(FakeTensor(..., size=(1, 1, 256, 256)), Parameter(FakeTensor(..., size=(14, 1, 512, 512), requires_grad=True)), Parameter(FakeTensor(..., size=(14,), requires_grad=True)), (2, 2), (1, 1), (1, 1), 1), **{}):
Calculated padded input size per channel: (258 x 258). Kernel size: (512 x 512). Kernel size can't be greater than actual input size

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
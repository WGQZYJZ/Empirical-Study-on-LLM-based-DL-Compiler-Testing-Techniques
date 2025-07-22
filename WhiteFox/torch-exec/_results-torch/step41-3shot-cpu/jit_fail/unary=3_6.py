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
        self.conv = torch.nn.Conv2d(12, 14, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(14, 5, 7, stride=2, padding=2)
        self.conv3 = torch.nn.Conv2d(5, 5, 11, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.conv2(v6)
        v8 = self.conv3(v7)
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 12, 26, 31)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (6 x 7). Kernel size: (11 x 11). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7fe7f2596ec0>(*(FakeTensor(..., size=(1, 5, ((s1 - 1)//4), ((s2 - 1)//4))), Parameter(FakeTensor(..., size=(5, 5, 11, 11), requires_grad=True)), Parameter(FakeTensor(..., size=(5,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (((s1 - 1)//4) x ((s2 - 1)//4)). Kernel size: (11 x 11). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 29, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
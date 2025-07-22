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
        self.conv1 = torch.nn.Conv2d(1, 46, 9, stride=1, padding=0)
        self.bn1 = torch.nn.BatchNorm2d(46)
        self.conv2 = torch.nn.Conv2d(46, 45, 15, stride=1, padding=0)
        self.bn2 = torch.nn.BatchNorm2d(45)

    def forward(self, x2):
        v1 = self.conv1(x2)
        v2 = self.bn1(v1)
        v3 = self.conv2(v2)
        v4 = self.bn2(v3)
        v5 = v4 * 0.5
        v6 = v4 * v4
        v7 = v6 * v4
        v8 = v7 * 0.044715
        v9 = v4 + v8
        v10 = v9 * 0.7978845608028654
        v11 = torch.tanh(v10)
        v12 = v11 + 1
        v13 = v5 * v12
        return v13



func = Model().to('cpu')


x2 = torch.randn(5, 1, 15, 18)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (7 x 10). Kernel size: (15 x 15). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7bfb43796ec0>(*(FakeTensor(..., size=(5, 46, 7, 10)), Parameter(FakeTensor(..., size=(45, 46, 15, 15), requires_grad=True)), Parameter(FakeTensor(..., size=(45,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (7 x 10). Kernel size: (15 x 15). Kernel size can't be greater than actual input size

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
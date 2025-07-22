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
        self.c1 = torch.nn.Conv2d(3, 32, 3)
        self.bn = torch.nn.BatchNorm2d(32)
        self.c2 = torch.nn.Conv2d(32, 32, 3)
        self.bn2 = torch.nn.BatchNorm2d(32)
        self.avgpool = torch.nn.AdaptiveAvgPool2d((32, 32))

    def forward(self, x):
        x = self.c1(x)
        x = self.bn(x)
        x = self.c2(x)
        x = self.bn2(x)
        return self.avgpool(x)



func = Model().to('cpu')


x = torch.randn(1, 3, 4, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2 x 2). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7f3f8d596ec0>(*(FakeTensor(..., size=(1, 32, 2, 2)), Parameter(FakeTensor(..., size=(32, 32, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (2 x 2). Kernel size: (3 x 3). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
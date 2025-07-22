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
        self.conv_1 = torch.nn.Conv2d(18, 20, 9, stride=2, padding=1)
        self.conv_2 = torch.nn.Conv2d(20, 16, 7, stride=3, padding=2)

    def forward(self, x1):
        v1 = self.conv_1(x1)
        v2 = self.conv_2(v1)
        v3 = v1 + v2
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 18, 3, 9)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (5 x 11). Kernel size: (9 x 9). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7bb142396ec0>(*(FakeTensor(..., size=(1, 18, 3, 9)), Parameter(FakeTensor(..., size=(20, 18, 9, 9), requires_grad=True)), Parameter(FakeTensor(..., size=(20,), requires_grad=True)), (2, 2), (1, 1), (1, 1), 1), **{}):
Calculated padded input size per channel: (5 x 11). Kernel size: (9 x 9). Kernel size can't be greater than actual input size

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
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
        self.conv_1 = torch.nn.Conv2d(1, 10, 5, stride=1)
        self.conv_2 = torch.nn.Conv2d(10, 1, 5, stride=1)

    def forward(self, x):
        v1 = self.conv_1(x)
        v2 = self.conv_2(v1)
        v3 = v2 > 0
        v4 = v2 * -0.5577
        v5 = torch.where(v3, v2, v4)
        return v5



func = Model().to('cpu')


x2 = torch.randn(1, 1, 2, 2, device='cuda')

test_inputs = [x2]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2 x 2). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7f044d596ec0>(*(FakeTensor(..., size=(1, 1, 2, 2)), Parameter(FakeTensor(..., size=(10, 1, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(10,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (2 x 2). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

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
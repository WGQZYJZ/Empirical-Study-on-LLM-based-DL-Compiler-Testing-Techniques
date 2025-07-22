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
        self.conv = torch.nn.Conv2d(26, 26, 4, 2, 0)

    def forward(self, x):
        x = self.conv(x)
        x = self.conv(x)
        return x



func = Model().to('cpu')


x = torch.randn(1, 26, 5, 5)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 1). Kernel size: (4 x 4). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7c4e6cb96ec0>(*(FakeTensor(..., size=(1, 26, 1, 1)), Parameter(FakeTensor(..., size=(26, 26, 4, 4), requires_grad=True)), Parameter(FakeTensor(..., size=(26,), requires_grad=True)), (2, 2), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (1 x 1). Kernel size: (4 x 4). Kernel size can't be greater than actual input size

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
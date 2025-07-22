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
        self.conv = nn.Conv3d(1, 1, 3)
        self.bn = nn.BatchNorm3d(1)

    def forward(self, x1):
        s = self.conv(x1)
        t = self.bn(s)
        return t



func = Model().to('cpu')


x1 = torch.randn(1, 1, 2, 4, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2 x 4 x 4). Kernel size: (3 x 3 x 3). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv3d of type object at 0x7ba015f96ec0>(*(FakeTensor(..., size=(1, 1, 2, s1, s2)), Parameter(FakeTensor(..., size=(1, 1, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (1, 1, 1), (0, 0, 0), (1, 1, 1), 1), **{}):
Calculated padded input size per channel: (2 x s1 x s2). Kernel size: (3 x 3 x 3). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 725, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 720, in _conv_forward
    return F.conv3d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        torch.manual_seed(1)
        self.conv = torch.nn.Conv3d(2, 5, 5)
        torch.manual_seed(1)
        self.bn = torch.nn.BatchNorm3d(5)

    def forward(self, x2):
        y2 = self.conv(x2)
        y2 = self.bn(y2)
        return y2 + y2



func = Model().to('cpu')


x2 = torch.randn(1, 2, 2, 2, 2)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (2 x 2 x 2). Kernel size: (5 x 5 x 5). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv3d of type object at 0x7b8b56f96ec0>(*(FakeTensor(..., size=(1, 2, s1, s2, s3)), Parameter(FakeTensor(..., size=(5, 2, 5, 5, 5), requires_grad=True)), Parameter(FakeTensor(..., size=(5,), requires_grad=True)), (1, 1, 1), (0, 0, 0), (1, 1, 1), 1), **{}):
Calculated padded input size per channel: (s1 x s2 x s3). Kernel size: (5 x 5 x 5). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 725, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 720, in _conv_forward
    return F.conv3d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
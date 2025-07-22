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
        self.conv1 = torch.nn.Conv3d(3, 3, 4)
        self.conv2 = torch.nn.Conv3d(3, 3, 3)
        self.conv3 = torch.nn.Conv3d(3, 3, 2)
        self.batchnorm3d = torch.nn.BatchNorm3d(3)

    def forward(self, x1):
        s = self.conv1(x1)
        t = self.conv2(s)
        t = self.conv3(t)
        t = self.batchnorm3d(t)
        return t



func = Model().to('cpu')


x1 = torch.randn(1, 3, 6, 6, 6)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 1 x 1). Kernel size: (2 x 2 x 2). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv3d of type object at 0x70248a796ec0>(*(FakeTensor(..., size=(1, 3, 1, 1, 1)), Parameter(FakeTensor(..., size=(3, 3, 2, 2, 2), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1, 1, 1), (0, 0, 0), (1, 1, 1), 1), **{}):
Calculated padded input size per channel: (1 x 1 x 1). Kernel size: (2 x 2 x 2). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 25, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 725, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 720, in _conv_forward
    return F.conv3d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
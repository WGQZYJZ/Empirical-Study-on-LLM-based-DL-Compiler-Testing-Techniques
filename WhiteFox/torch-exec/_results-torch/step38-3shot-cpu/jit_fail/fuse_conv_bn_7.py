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
        self.conv = torch.nn.Conv2d(20, 20, kernel_size=(5, 5), stride=(2, 2), bias=False)
        self.batch_norm_0 = torch.nn.BatchNorm2d(20, affine=True)
        self.conv_1 = torch.nn.Conv2d(20, 40, kernel_size=(5, 5), stride=(1, 1), bias=False)
        self.batch_norm_1 = torch.nn.BatchNorm2d(40, affine=True)

    def forward(self, x):
        x = self.conv(x)
        x = self.batch_norm_0(x)
        x = self.conv_1(x)
        x = self.batch_norm_1(x)
        return x



func = Model().to('cpu')


x = torch.randn(1, 20, 6, 6)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (1 x 1). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x72741f196ec0>(*(FakeTensor(..., size=(1, 20, 1, 1)), Parameter(FakeTensor(..., size=(40, 20, 5, 5), requires_grad=True)), None, (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (1 x 1). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

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
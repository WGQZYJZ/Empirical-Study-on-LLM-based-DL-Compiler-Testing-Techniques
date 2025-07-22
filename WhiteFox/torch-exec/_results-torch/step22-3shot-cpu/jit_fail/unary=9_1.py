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
        self.conv = torch.nn.Conv2d(3, 3, 9)

    def forward(self, x1):
        x1 = torch.nn.functional.hardtanh(x1 + 3.0, min_val=-3.0, max_val=0.0)
        x1 = torch.nn.functional.interpolate(x1, scale_factor=0.0625, mode='nearest')
        x1 = self.conv(x1)
        x1 = torch.nn.functional.relu6(x1)
        x1 = torch.nn.functional.softmax(x1, dim=0)
        return x1



func = Model().to('cpu')


x1 = torch.randn(2, 3, 128, 128)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (8 x 8). Kernel size: (9 x 9). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7d7af2196ec0>(*(FakeTensor(...,
           size=(s0, 3, TruncToInt(0.0625*ToFloat(s2)), TruncToInt(0.0625*ToFloat(s3)))), Parameter(FakeTensor(..., size=(3, 3, 9, 9), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (TruncToInt(0.0625*ToFloat(s2)) x TruncToInt(0.0625*ToFloat(s3))). Kernel size: (9 x 9). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
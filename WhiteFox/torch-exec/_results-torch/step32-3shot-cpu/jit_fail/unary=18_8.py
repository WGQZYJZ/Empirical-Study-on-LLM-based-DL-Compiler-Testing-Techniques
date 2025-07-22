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
        self.conv1 = torch.nn.Conv2d(32, 64, kernel_size=(6, 3))
        self.conv2 = torch.nn.Conv2d(64, 64, kernel_size=(100, 3), padding=18, dilation=4)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv2(v2)
        v4 = torch.sigmoid(v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 32, 17, 17)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (48 x 51). Kernel size: (397 x 9). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x77ed21996ec0>(*(FakeTensor(..., size=(1, 64, 12, 15)), Parameter(FakeTensor(..., size=(64, 64, 100, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(64,), requires_grad=True)), (1, 1), (18, 18), (4, 4), 1), **{}):
Calculated padded input size per channel: (48 x 51). Kernel size: (397 x 9). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
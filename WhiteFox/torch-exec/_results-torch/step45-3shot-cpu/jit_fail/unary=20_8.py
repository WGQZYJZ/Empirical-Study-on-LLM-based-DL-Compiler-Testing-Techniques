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
        self.conv_t1 = torch.nn.ConvTranspose2d(1, 16, kernel_size=1, stride=1, padding=0, bias=False)
        self.conv1 = torch.nn.Conv2d(16, 16, kernel_size=3, stride=1, padding=1, dilation=2, bias=False)

    def forward(self, x1):
        v1 = self.conv_t1(x1)
        v2 = self.conv1(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 1, 1, 1)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (3 x 3). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7dece2196ec0>(*(FakeTensor(..., size=(1, 16, 1, 1)), Parameter(FakeTensor(..., size=(16, 16, 3, 3), requires_grad=True)), None, (1, 1), (1, 1), (2, 2), 1), **{}):
Calculated padded input size per channel: (3 x 3). Kernel size: (5 x 5). Kernel size can't be greater than actual input size

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
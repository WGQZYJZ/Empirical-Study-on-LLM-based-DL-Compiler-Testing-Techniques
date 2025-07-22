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
        self.conv1 = torch.nn.Conv2d(24, 48, (1, 5), stride=(4, 1), padding=(1, 2))
        self.conv2 = torch.nn.Conv2d(48, 96, (1, 10), stride=(1, 5), padding=(0, 7))
        self.conv3 = torch.nn.Conv2d(96, 192, (1, 20), stride=(1, 10), padding=(0, 6))

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        return v3



func = Model().to('cpu')


x = torch.randn(1, 24, 47, 26)

test_inputs = [x]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (13 x 19). Kernel size: (1 x 20). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x78e6ba596ec0>(*(FakeTensor(..., size=(1, 96, 13, 7)), Parameter(FakeTensor(..., size=(192, 96, 1, 20), requires_grad=True)), Parameter(FakeTensor(..., size=(192,), requires_grad=True)), (1, 10), (0, 6), (1, 1), 1), **{}):
Calculated padded input size per channel: (13 x 19). Kernel size: (1 x 20). Kernel size can't be greater than actual input size

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 554, in forward
    return self._conv_forward(input, self.weight, self.bias)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/conv.py", line 549, in _conv_forward
    return F.conv2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
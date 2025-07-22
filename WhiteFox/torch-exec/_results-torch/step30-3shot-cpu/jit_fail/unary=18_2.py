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
        self.conv1 = torch.nn.Conv2d(1, 64, (64, 32), stride=(62, 30), padding=(0, 0))
        self.conv2 = torch.nn.Conv2d(64, 256, (16, 21), stride=(16, 21), padding=(0, 0))

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.sigmoid(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 1, 512, 211)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Calculated padded input size per channel: (8 x 6). Kernel size: (16 x 21). Kernel size can't be greater than actual input size

jit:
Failed running call_function <built-in method conv2d of type object at 0x7e741ab96ec0>(*(FakeTensor(..., size=(1, 64, 8, 6)), Parameter(FakeTensor(..., size=(256, 64, 16, 21), requires_grad=True)), Parameter(FakeTensor(..., size=(256,), requires_grad=True)), (16, 21), (0, 0), (1, 1), 1), **{}):
Calculated padded input size per channel: (8 x 6). Kernel size: (16 x 21). Kernel size can't be greater than actual input size

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
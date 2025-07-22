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
        self.conv0 = torch.nn.Conv2d(3, 24, 1, stride=1, padding=0)
        self.avgpool = torch.nn.AvgPool2d(3, stride=1, padding=0)
        self.conv = torch.nn.Conv2d(24, 32, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.avgpool(x1)
        v2 = self.conv(v1)
        t1 = self.conv0(x1).unsqueeze(1)
        v3 = v2 + t1
        v4 = torch.clamp_min(v3, 0)
        v5 = torch.clamp_max(v4, 6)
        v6 = v1 * v5
        v7 = v6 / 6
        return v7.unsqueeze(0)



func = Model().to('cpu')


x1 = torch.randn(1, 3, 128, 128)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [32, 24, 1, 1], expected input[1, 3, 126, 126] to have 24 channels, but got 3 channels instead

jit:
Failed running call_function <built-in method conv2d of type object at 0x76a85f196ec0>(*(FakeTensor(..., size=(1, 3, 126, 126)), Parameter(FakeTensor(..., size=(32, 24, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(32,), requires_grad=True)), (1, 1), (0, 0), (1, 1), 1), **{}):
Given groups=1, weight of size [32, 24, 1, 1], expected input[1, 3, 126, 126] to have 24 channels, but got 3 channels instead

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
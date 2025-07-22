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
        self.conv = torch.nn.Conv3d(3, 3, 3, stride=0, padding=0, dilation=1)
        self.maxpool = torch.nn.MaxPool3d(2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = 3 + v1
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v1 * v4
        v6 = v5 / 6
        v7 = self.maxpool(v6)
        return v7



func = Model().to('cpu')


x1 = torch.randn(2, 3, 7, 7, 7)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
non-positive stride is not supported

jit:
Failed running call_function <built-in method conv3d of type object at 0x72c860f96ec0>(*(FakeTensor(..., size=(s0, s1, s2, s3, s4)), Parameter(FakeTensor(..., size=(3, 3, 3, 3, 3), requires_grad=True)), Parameter(FakeTensor(..., size=(3,), requires_grad=True)), (0, 0, 0), (0, 0, 0), (1, 1, 1), 1), **{}):
non-positive stride is not supported

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
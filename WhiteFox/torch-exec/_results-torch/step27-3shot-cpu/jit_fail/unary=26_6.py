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

    def __init__(self, negative_slope=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(123, 1, 1, stride=0)
        self.conv_t = torch.nn.ConvTranspose2d(1, 1, 2, stride=0, output_padding=0)
        self.negative_slope = negative_slope

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.negative_slope if self.negative_slope else 0.01
        v3 = self.conv_t(v1)
        v4 = v3 >= 0
        v5 = v3 * v2
        v6 = torch.where(v4, v3, v5)
        return v6



func = Model().to('cpu')


x = torch.randn(1, 123, 18, 18)

test_inputs = [x]

# JIT_FAIL
'''
direct:
non-positive stride is not supported

jit:
Failed running call_function <built-in method conv2d of type object at 0x736832996ec0>(*(FakeTensor(..., size=(1, 123, 18, 18)), Parameter(FakeTensor(..., size=(1, 123, 1, 1), requires_grad=True)), Parameter(FakeTensor(..., size=(1,), requires_grad=True)), (0, 0), (0, 0), (1, 1), 1), **{}):
non-positive stride is not supported

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
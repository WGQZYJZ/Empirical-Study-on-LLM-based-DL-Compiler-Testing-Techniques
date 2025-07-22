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
        self.avg_pool2d = torch.nn.AvgPool2d(3, stride=1, padding=2, count_include_pad=False)
        self.conv = torch.nn.Conv2d(256, 16, 7, stride=1, padding=0)

    def forward(self, x1):
        v1 = x1
        v2 = self.avg_pool2d(v1)
        v3 = self.conv(v2)
        v4 = v3 + 3
        v5 = torch.clamp(v4, min=0, max=6)
        v6 = v3 * v5
        v7 = v6 / 6
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 256, 14, 14)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of effective kernel size, but got pad=2, kernel_size=3 and dilation=1

jit:
Failed running call_function <built-in function avg_pool2d>(*(FakeTensor(..., size=(1, 256, 14, 14)), 3, 1, 2, False, False, None), **{}):
pad should be at most half of effective kernel size, but got pad=2, kernel_size=3 and dilation=1

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/pooling.py", line 756, in forward
    return F.avg_pool2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
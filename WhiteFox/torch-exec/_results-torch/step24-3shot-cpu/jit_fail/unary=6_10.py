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
        self.max = torch.nn.MaxPool2d(3, stride=1, padding=2)

    def forward(self, x1):
        v1 = self.max(x1) + 3
        v2 = torch.clamp(v1, min=0, max=6)
        v3 = torch.mul(v2, 4.0)
        v4 = v3 / 5
        return v4



func = Model().to('cpu')


x1 = torch.randn(6, 3, 14, 14)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of effective kernel size, but got pad=2, kernel_size=3 and dilation=1

jit:
Failed running call_function <function boolean_dispatch.<locals>.fn at 0x7d8b0ba60ee0>(*(FakeTensor(..., size=(s0, s1, s2, s3)), 3, 1, 2, 1), **{'ceil_mode': False, 'return_indices': False}):
pad should be at most half of effective kernel size, but got pad=2, kernel_size=3 and dilation=1

from user code:
   File "<string>", line 20, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/pooling.py", line 213, in forward
    return F.max_pool2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
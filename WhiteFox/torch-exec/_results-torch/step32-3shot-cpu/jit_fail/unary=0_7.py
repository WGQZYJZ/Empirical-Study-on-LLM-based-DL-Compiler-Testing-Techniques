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
        self.conv = torch.nn.Conv2d(3, 1, 2, stride=1)
        self.pool = torch.nn.AvgPool2d(3, stride=2, padding=3, count_include_pad=False)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * v1
        v4 = v3 * v1
        v5 = v4 * 0.044715
        v6 = v1 + v5
        v7 = v6 * 0.7978845608028654
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v2 * v9
        v11 = self.pool(v10)
        return v11



func = Model().to('cpu')


x1 = torch.randn(1, 3, 257, 256)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of effective kernel size, but got pad=3, kernel_size=3 and dilation=1

jit:
Failed running call_function <built-in function avg_pool2d>(*(FakeTensor(..., size=(1, 1, s1 - 1, s2 - 1)), 3, 2, 3, False, False, None), **{}):
pad should be at most half of effective kernel size, but got pad=3, kernel_size=3 and dilation=1

from user code:
   File "<string>", line 31, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/pooling.py", line 756, in forward
    return F.avg_pool2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def __init__(self, min_value=1, max_value=631):
        super().__init__()
        self.max_pool = torch.nn.MaxPool2d(10, 1, padding=10)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.max_pool(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 3, 192, 811)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of effective kernel size, but got pad=10, kernel_size=10 and dilation=1

jit:
Failed running call_function <function boolean_dispatch.<locals>.fn at 0x7831ebea1ee0>(*(FakeTensor(..., size=(1, 3, 192, 811)), 10, 1, 10, 1), **{'ceil_mode': False, 'return_indices': False}):
pad should be at most half of effective kernel size, but got pad=10, kernel_size=10 and dilation=1

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/pooling.py", line 213, in forward
    return F.max_pool2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
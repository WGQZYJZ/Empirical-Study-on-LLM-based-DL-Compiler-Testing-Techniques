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

    def __init__(self, min, max):
        super().__init__()
        self.conv = torch.nn.Conv1d(13, 10, 11, stride=3, dilation=2)
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = torch.nn.functional.avg_pool2d(x1, 3, stride=2, padding=2)
        v2 = self.conv(v1)
        v3 = torch.clamp_min(v2, self.min)
        v4 = torch.clamp_max(v3, self.max)
        return v4


min = 0.6
max = 1.6

func = Model(min, max).to('cpu')


x1 = torch.randn(1, 13, 100)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of effective kernel size, but got pad=2, kernel_size=3 and dilation=1

jit:
Failed running call_function <built-in function avg_pool2d>(*(FakeTensor(..., size=(1, s0, s1)), 3), **{'stride': 2, 'padding': 2}):
pad should be at most half of effective kernel size, but got pad=2, kernel_size=3 and dilation=1

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
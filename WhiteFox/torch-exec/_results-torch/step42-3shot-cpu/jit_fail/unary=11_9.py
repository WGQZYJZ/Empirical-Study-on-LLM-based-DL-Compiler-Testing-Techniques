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
        self.conv_transpose = torch.nn.ConvTranspose2d(2, 2, 5, stride=3, padding=1)
        self.avg_pool2d = torch.nn.AvgPool2d(2, stride=2, padding=5)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        v6 = self.avg_pool2d(v5)
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 2, 30, 30)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of effective kernel size, but got pad=5, kernel_size=2 and dilation=1

jit:
Failed running call_function <built-in function avg_pool2d>(*(FakeTensor(..., size=(1, 2, 3*s1, 3*s2)), 2, 2, 5, False, True, None), **{}):
pad should be at most half of effective kernel size, but got pad=5, kernel_size=2 and dilation=1

from user code:
   File "<string>", line 26, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/pooling.py", line 756, in forward
    return F.avg_pool2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
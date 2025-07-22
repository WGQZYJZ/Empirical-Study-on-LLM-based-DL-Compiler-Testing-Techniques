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
        self.avg_pool = torch.nn.AvgPool2d(kernel_size=2, stride=1, padding=0)
        self.avg_pool_1 = torch.nn.AvgPool2d(kernel_size=1, stride=1, padding=1)
        self.avg_pool_2 = torch.nn.AvgPool2d(kernel_size=1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.avg_pool(x1)
        v2 = self.avg_pool_1(v1)
        v3 = self.avg_pool_2(v1)
        v4 = torch.tanh(v2)
        v5 = torch.mul(v2, v3)
        v6 = torch.add(v4, v5)
        v7 = torch.mul(x1, v6)
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 3, 18, 18)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of effective kernel size, but got pad=1, kernel_size=1 and dilation=1

jit:
Failed running call_function <built-in function avg_pool2d>(*(FakeTensor(..., size=(1, 3, 17, 17)), 1, 1, 1, False, True, None), **{}):
pad should be at most half of effective kernel size, but got pad=1, kernel_size=1 and dilation=1

from user code:
   File "<string>", line 23, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/pooling.py", line 756, in forward
    return F.avg_pool2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
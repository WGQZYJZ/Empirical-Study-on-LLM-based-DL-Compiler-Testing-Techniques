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
        self.sigmoid = torch.nn.Sigmoid()
        self.conv = torch.nn.Conv2d(3, 16, 3, stride=2, padding=1)
        self.avg = torch.nn.AvgPool2d(4, stride=4, padding=59)

    def forward(self, x):
        v = self.conv(x)
        v = self.sigmoid(v)
        v = self.avg(v)
        return v



func = Model().to('cpu')


x = torch.randn(1, 3, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
pad should be at most half of effective kernel size, but got pad=59, kernel_size=4 and dilation=1

jit:
Failed running call_function <built-in function avg_pool2d>(*(FakeTensor(..., size=(1, 16, 32, 32)), 4, 4, 59, False, True, None), **{}):
pad should be at most half of effective kernel size, but got pad=59, kernel_size=4 and dilation=1

from user code:
   File "<string>", line 24, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/pooling.py", line 756, in forward
    return F.avg_pool2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.features = torch.nn.Sequential(torch.nn.MaxPool2d(3, 2, 1, 1), torch.nn.MaxPool2d(5, 4, 2, 2), torch.nn.MaxPool2d(3, 1, 1, 0))
        self.convolution = torch.nn.Conv2d(3, 3, 3, 1, 1)

    def forward(self, x1):
        v1 = self.features(x1)
        v1 = self.convolution(v1)
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
pad should be at most half of effective kernel size, but got pad=1, kernel_size=3 and dilation=0

jit:
Failed running call_function <function boolean_dispatch.<locals>.fn at 0x73ffcec61ee0>(*(FakeTensor(..., size=(1, s0, ((s1 - 1)//8), ((s2 - 1)//8))), 3, 1, 1, 0), **{'ceil_mode': False, 'return_indices': False}):
pad should be at most half of effective kernel size, but got pad=1, kernel_size=3 and dilation=0

from user code:
   File "<string>", line 21, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/pooling.py", line 213, in forward
    return F.max_pool2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
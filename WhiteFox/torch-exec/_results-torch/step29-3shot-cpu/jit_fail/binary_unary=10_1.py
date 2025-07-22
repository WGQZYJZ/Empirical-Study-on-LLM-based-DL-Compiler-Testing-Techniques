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
        self.conv = torch.nn.Sequential(torch.nn.Conv2d(3, 8, 1, stride=1, padding=1), torch.nn.BatchNorm2d(8), torch.nn.MaxPool2d(128))
        self.linear = torch.nn.Linear(8, 4096)
        self.linear2 = torch.nn.Linear(4096, 4096)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.linear(v1)
        v3 = self.linear2(v2)
        v4 = v3 + v1
        return v4


func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given input size: (8x66x66). Calculated output size: (8x0x0). Output size is too small

jit:
Failed running call_function <function boolean_dispatch.<locals>.fn at 0x7a3834d21ee0>(*(FakeTensor(..., size=(1, 8, 66, 66)), 128, 128, 0, 1), **{'ceil_mode': False, 'return_indices': False}):
Given input size: (8x66x66). Calculated output size: (8x0x0). Output size is too small

from user code:
   File "<string>", line 22, in forward
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/container.py", line 250, in forward
    input = module(input)
  File "/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/torch/nn/modules/pooling.py", line 213, in forward
    return F.max_pool2d(


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
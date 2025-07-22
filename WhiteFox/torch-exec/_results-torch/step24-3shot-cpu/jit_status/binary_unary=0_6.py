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
        self.conv = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)

    def forward(self, x1, x2, x3, x4, x5, x6, x7, x8, x9):
        v1 = self.conv(x1)
        v2 = v1 + x2
        v3 = torch.relu(v2)
        v4 = x3 + x4
        v5 = v3 + v4
        v6 = torch.relu(v5)
        v7 = x5 + x6
        v8 = v6 + v7
        v9 = torch.relu(v8)
        v10 = x7 + x8
        v11 = v9 + v10
        v12 = torch.relu(v11)
        v13 = x9 + v12
        v14 = torch.relu(v13)
        return v14



func = Model().to('cpu')


x1 = torch.randn(1, 16, 64, 64)

x2 = torch.randn(1, 16, 64, 64)

x3 = torch.randn(1, 16, 64, 64)

x4 = torch.randn(1, 16, 64, 64)

x5 = torch.randn(1, 16, 64, 64)

x6 = torch.randn(1, 16, 64, 64)

x7 = torch.randn(1, 16, 64, 64)

x8 = torch.randn(1, 16, 64, 64)

x9 = torch.randn(1, 16, 64, 64)

test_inputs = [x1, x2, x3, x4, x5, x6, x7, x8, x9]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmprb6p1tog/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmprb6p1tog/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmprb6p1tog', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
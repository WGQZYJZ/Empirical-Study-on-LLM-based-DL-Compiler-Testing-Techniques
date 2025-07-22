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
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)

    def forward(self, x1, x2, x3):
        v1 = torch.sigmoid(x1)
        v2 = self.conv1(v1)
        v3 = torch.relu(x2)
        v4 = v2 + v3
        v5 = self.conv2(v4)
        v6 = v5 + x3
        v7 = torch.sigmoid(v6)
        return v7



func = Model().to('cuda')


x2 = torch.randn(1, 16, 64, 64)

x3 = torch.randn(1, 16, 64, 64)
x1 = 1

test_inputs = [x2, x3, x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmproj3bth9/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmproj3bth9/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmproj3bth9', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
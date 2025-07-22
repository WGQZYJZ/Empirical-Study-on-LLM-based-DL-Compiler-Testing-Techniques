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
        self.conv = torch.nn.Conv2d(9, 6, 1, stride=1, padding=1)

    def forward(self, input=None, padding1=None, other=None, t3=None):
        if input is None:
            input = torch.randn(1, 9, 64, 64)
        x1 = self.conv(input)
        if other == None:
            other = torch.randn(x1.shape)
        v2 = x1 + other
        if padding1 == None:
            padding1 = torch.randn(v2.shape)
        v3 = v2 + padding1
        if t3 == None:
            t3 = torch.randn(v3.shape)
        v4 = v3 + t3
        return v4



func = Model().to('cpu')


input = torch.randn(1, 9, 64, 64)

test_inputs = [input]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpw6pvns84/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpw6pvns84/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpw6pvns84', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
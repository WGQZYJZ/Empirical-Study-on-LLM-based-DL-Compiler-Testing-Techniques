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

    def __init__(self, min_value=1.2, max_value=6.0):
        super().__init__()
        self.conv_transpose1 = torch.nn.ConvTranspose1d(32, 32, kernel_size=3, stride=1, padding=1)
        self.conv_transpose2 = torch.nn.ConvTranspose1d(32, 64, kernel_size=3, stride=1, padding=1)
        self.conv_transpose3 = torch.nn.ConvTranspose1d(64, 64, kernel_size=5, stride=1, padding=2)
        self.conv_transpose4 = torch.nn.ConvTranspose1d(64, 64, kernel_size=3, stride=1, padding=1)
        self.conv_transpose1 = torch.nn.ConvTranspose1d(32, 32, kernel_size=3, stride=1, padding=1)
        self.conv_transpose2 = torch.nn.ConvTranspose1d(32, 64, kernel_size=3, stride=1, padding=1)
        self.conv_transpose3 = torch.nn.ConvTranspose1d(64, 64, kernel_size=5, stride=1, padding=2)
        self.conv_transpose4 = torch.nn.ConvTranspose1d(64, 64, kernel_size=3, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x):
        v1 = self.conv_transpose1(x)
        v3 = torch.clamp_min(v1, self.min_value)
        v4 = self.conv_transpose2(v3)
        v6 = torch.clamp_max(v4, self.max_value)
        v7 = self.conv_transpose3(v6)
        v9 = torch.clamp_min(v7, self.min_value)
        v10 = self.conv_transpose3(v9)
        v12 = torch.clamp_max(v10, self.max_value)
        v13 = self.conv_transpose3(v12)
        v15 = torch.clamp_min(v13, self.min_value)
        v16 = self.conv_transpose3(v15)
        v18 = torch.clamp_max(v16, self.max_value)
        return v18



func = Model().to('cpu')


x1 = torch.randn(1, 32, 2048)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp2xq4w3oy/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp2xq4w3oy/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp2xq4w3oy', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
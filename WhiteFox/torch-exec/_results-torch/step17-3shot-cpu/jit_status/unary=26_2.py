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

    def __init__(self, n_channels):
        super().__init__()
        self.conv_t1 = torch.nn.ConvTranspose2d(n_channels, 256, kernel_size=(4, 8))
        self.conv_t2 = torch.nn.ConvTranspose2d(256, n_channels, kernel_size=(3, 8))

    def forward(self, x2):
        v1 = self.conv_t1(x2)
        v2 = v1 > 0
        v3 = v1 * 0.25
        v4 = torch.where(v2, v1, v3)
        v5 = self.conv_t2(v4)
        return v5


n_channels = 3

func = Model(n_channels).to('cpu')


n_channels = 3
x2 = torch.randn(8, n_channels, 8, 8)

test_inputs = [x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpzuf8pgat/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpzuf8pgat/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpzuf8pgat', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
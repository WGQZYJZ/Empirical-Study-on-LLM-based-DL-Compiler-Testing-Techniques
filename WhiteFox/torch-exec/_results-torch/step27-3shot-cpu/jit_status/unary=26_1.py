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

    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.Conv2d(6, 8, 8, stride=8, padding=8)
        self.conv_t = torch.nn.ConvTranspose2d(8, 14, 7, stride=7, padding=7)
        self.negative_slope = negative_slope

    def forward(self, x, weight):
        y = self.conv(x)
        z = self.conv_t(y)
        m = z > 0
        n = z * self.negative_slope
        o = torch.where(m, z, n)
        return (o, weight)


negative_slope = 0.007

func = Model(negative_slope).to('cpu')


x = torch.randn(1, 6, 1, 1)

weight = torch.randn(7, 7)

test_inputs = [x, weight]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpxnamb1ag/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpxnamb1ag/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpxnamb1ag', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
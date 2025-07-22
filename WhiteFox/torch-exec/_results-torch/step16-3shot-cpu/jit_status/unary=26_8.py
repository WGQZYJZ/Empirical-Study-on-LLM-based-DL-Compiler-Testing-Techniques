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
        self.conv_t1 = torch.nn.ConvTranspose2d(9, 16, 1, stride=1, padding=0, bias=False)
        self.conv_t2 = torch.nn.ConvTranspose2d(16, 32, 1, stride=2, padding=0, bias=False)
        self.conv_t3 = torch.nn.ConvTranspose2d(32, 1, 1, stride=1, padding=0, bias=False)
        self.negative_slope = negative_slope

    def forward(self, x3):
        a1 = self.conv_t1(x3)
        a2 = a1 > 0
        a3 = a1 * self.negative_slope
        a4 = torch.where(a2, a1, a3)
        a5 = self.conv_t2(a4)
        a6 = a5 > 0
        a7 = a5 * self.negative_slope
        a8 = torch.where(a6, a5, a7)
        a9 = self.conv_t3(a8)
        aa = a9 > 0
        ab = a9 * self.negative_slope
        ac = torch.where(aa, a9, ab)
        return ac


negative_slope = -0.1

func = Model(negative_slope).to('cpu')


x3 = torch.randn(4, 9, 8, 8)

test_inputs = [x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp7qv0vxh1/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp7qv0vxh1/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp7qv0vxh1', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
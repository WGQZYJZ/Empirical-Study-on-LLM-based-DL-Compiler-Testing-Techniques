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
        self.conv_t1 = torch.nn.ConvTranspose2d(19, 64, 1, stride=1, padding=0)
        self.conv_t2 = torch.nn.ConvTranspose2d(64, 19, 1, stride=1, padding=0)
        self.conv_t3 = torch.nn.ConvTranspose2d(19, 19, 1, stride=1, padding=0)
        self.negative_slope = negative_slope

    def forward(self, x6):
        x7 = self.conv_t1(x6)
        x8 = self.conv_t2(x7)
        x9 = self.conv_t3(x8)
        x10 = x9 > 0
        x11 = x9 * self.negative_slope
        x12 = torch.where(x10, x9, x11)
        return x12


negative_slope = -0.1

func = Model(negative_slope).to('cpu')


x6 = torch.randn(2, 19, 4, 4)

test_inputs = [x6]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpcl1o27of/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpcl1o27of/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpcl1o27of', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
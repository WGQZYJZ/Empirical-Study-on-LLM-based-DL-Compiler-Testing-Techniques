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
        self.conv = torch.nn.Conv2d(39, 1, (1, 7), stride=(5, 2))
        self.conv_t_neg = torch.nn.ConvTranspose2d(1, 1, (1, 6), stride=(5, 1))
        self.conv_t_pos = torch.nn.ConvTranspose2d(1, 1, (1, 7), stride=(1, 7))
        self.negative_slope = negative_slope

    def forward(self, x):
        y = self.conv(x)
        z1 = self.conv_t_neg(y)
        z2 = self.conv_t_pos(z1)
        m1 = z2 > 0
        m2 = z2 * self.negative_slope
        m3 = torch.where(m1, z2, m2)
        return m3


negative_slope = 0.6619

func = Model(negative_slope).to('cpu')


x = torch.randn(1, 39, 54, 56)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp7jfzo9pv/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp7jfzo9pv/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp7jfzo9pv', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
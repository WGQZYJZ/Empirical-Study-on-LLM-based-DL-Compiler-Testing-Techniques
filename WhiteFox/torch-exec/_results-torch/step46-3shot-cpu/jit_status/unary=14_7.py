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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(64, 64, 3, stride=1, padding=1, dilation=1, groups=1)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(64, 64, 3, stride=1, padding=1, dilation=1, groups=1)

    def forward(self, x1):
        t1 = self.conv_transpose_1(x1)
        t2 = torch.tanh(t1)
        t3 = self.conv_transpose_2(t2)
        t4 = torch.sigmoid(t3)
        t5 = t2 + t4
        t6 = torch.sigmoid(t5)
        t7 = t5 * t6
        return t7



func = Model().to('cpu')


x1 = torch.randn(1, 64, 31, 31)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpknpyrhmb/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpknpyrhmb/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpknpyrhmb', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
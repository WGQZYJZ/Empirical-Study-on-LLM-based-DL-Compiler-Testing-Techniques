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
        self.conv_transpose_8 = torch.nn.ConvTranspose2d(2, 40, 4, stride=2, padding=1)
        self.conv_transpose_10 = torch.nn.ConvTranspose2d(40, 20, 7, stride=2, padding=2)
        self.conv_transpose_12 = torch.nn.ConvTranspose2d(20, 8, 16, stride=2, padding=4)
        self.conv_transpose_14 = torch.nn.ConvTranspose2d(8, 1, 7, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose_8(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        v4 = self.conv_transpose_10(v3)
        v5 = torch.sigmoid(v4)
        v6 = v4 * v5
        v7 = self.conv_transpose_12(v6)
        v8 = torch.sigmoid(v7)
        v9 = v7 * v8
        v10 = self.conv_transpose_14(v9)
        return v10



func = Model().to('cpu')


x1 = torch.randn(1, 2, 14, 14)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmphgriw9t4/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmphgriw9t4/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmphgriw9t4', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
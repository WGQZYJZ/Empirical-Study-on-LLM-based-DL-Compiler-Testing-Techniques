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
        self.conv_transpose_0 = torch.nn.ConvTranspose2d(210, 34, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(34, 69, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(69, 34, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))
        self.conv_transpose_3 = torch.nn.ConvTranspose2d(34, 97, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))
        self.conv_transpose_4 = torch.nn.ConvTranspose2d(97, 210, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))

    def forward(self, x1):
        v1 = self.conv_transpose_0(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        v4 = self.conv_transpose_1(v3)
        v5 = torch.sigmoid(v4)
        v6 = v4 * v5
        v7 = self.conv_transpose_2(v6)
        v8 = torch.sigmoid(v7)
        v9 = v7 * v8
        v10 = self.conv_transpose_3(v9)
        v11 = torch.sigmoid(v10)
        v12 = v10 * v11
        v13 = self.conv_transpose_4(v12)
        return v13



func = Model().to('cpu')


x1 = torch.randn(2, 210, 32, 32)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpcup5in7o/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpcup5in7o/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpcup5in7o', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
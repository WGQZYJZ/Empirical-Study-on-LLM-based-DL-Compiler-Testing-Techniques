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
        self.softmax = torch.nn.Softmax(dim=-1)
        self.conv2d = torch.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=3, stride=1, padding=0)
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1, output_padding=0)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(in_channels=32, out_channels=32, kernel_size=3, stride=2, padding=1, output_padding=1)
        self.conv_transpose_3 = torch.nn.ConvTranspose2d(in_channels=32, out_channels=32, kernel_size=3, stride=2, padding=1, output_padding=1)

    def forward(self, x1):
        v1 = self.softmax(x1)
        v2 = self.conv2d(v1)
        v3 = self.conv_transpose_1(v2)
        v4 = self.conv_transpose_2(v3)
        v5 = self.conv_transpose_3(v4)
        v6 = self.softmax(v5)
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 3, 108, 108)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp0yzk1m6a/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp0yzk1m6a/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp0yzk1m6a', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 1, 1, stride=2, padding=1, dilation=1, bias=False, groups=1)
        self.batch_norm = torch.nn.BatchNorm2d(1)
        self.conv = torch.nn.Conv2d(1, 1, 3, stride=1, padding=1)
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 1, 3, stride=1, padding=1, dilation=1, output_padding=1, groups=1)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.batch_norm(v1)
        v3 = self.conv(v2)
        v4 = self.conv_transpose(v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 1, 4, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_height: 1 output_padding_width: 1 stride_height: 1 stride_width: 1 dilation_height: 1 dilation_width: 1

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpllzs1c56/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpllzs1c56/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpllzs1c56', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
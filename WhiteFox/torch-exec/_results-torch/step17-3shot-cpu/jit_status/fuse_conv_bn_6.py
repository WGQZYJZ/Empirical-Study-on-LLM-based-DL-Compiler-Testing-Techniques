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

class ConvBlock(nn.Module):

    def __init__(self):
        super(ConvBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=8, kernel_size=3, padding=1, bias=False)
        self.bn = nn.BatchNorm2d(8, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn(x)
        return x

class Model(nn.Module):

    def __init__(self):
        super(Model, self).__init__()
        self.convblock = ConvBlock()
        self.batch_norm = nn.BatchNorm2d(8, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.conv = nn.Conv2d(in_channels=8, out_channels=8, kernel_size=3, padding=1, bias=False)

    @torch.no_grad()
    def forward(self, x):
        x = self.convblock(x)
        x = self.batch_norm(x)
        x = self.conv(x)
        return x



func = Model().to('cpu')


x = torch.randn(1, 1, 4, 4)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp18thqdf4/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp18thqdf4/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp18thqdf4', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
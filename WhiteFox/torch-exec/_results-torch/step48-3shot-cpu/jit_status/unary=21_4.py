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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(7, 49, 3, stride=2, padding=2)
        self.conv1 = torch.nn.Conv2d(49, 49, 3, dilation=2, padding=2)
        self.softmax = torch.nn.Softmax(dim=-1)
        self.conv2 = torch.nn.Conv2d(49, 1, 1, padding=0)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.conv1(v1)
        v3 = self.softmax(v2)
        v4 = self.conv2(v3)
        v5 = torch.tanh(v4)
        return v5



func = ModelTanh().to('cpu')


x = torch.randn(49, 7, 33, 98)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpq3u2k5fi/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpq3u2k5fi/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpq3u2k5fi', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
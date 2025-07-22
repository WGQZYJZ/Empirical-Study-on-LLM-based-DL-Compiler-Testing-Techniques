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
        self.conv = torch.nn.Conv2d(3, 1, 3)
        self.conv1x1 = torch.nn.Conv2d(1, 1, 1)
        self.conv3x3 = torch.nn.Conv2d(1, 1, 3, stride=2, padding=1, dilation=2, groups=1)
        self.tanh = torch.nn.Tanh()

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.conv1x1(v1)
        v3 = self.conv3x3(v2)
        v4 = self.tanh(v3)
        v5 = torch.zeros_like(v4)
        return v5



func = ModelTanh().to('cpu')


x = torch.randn(10, 3, 24, 24)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpfjkzukfw/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpfjkzukfw/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpfjkzukfw', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
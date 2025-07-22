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

    def __init__(self, in_channels, conv_dim, out_channels):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose1d(in_channels, out_channels, 3, stride=conv_dim)

    def forward(self, x):
        y = self.conv1(x)
        z = torch.tanh(y)
        return z


in_channels = 1
conv_dim = 1
out_channels = 1

func = ModelTanh(in_channels, conv_dim, out_channels).to('cpu')


x = torch.empty(3, 3, 3).uniform_()

test_inputs = [x]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [1, 1, 3], expected input[3, 3, 3] to have 1 channels, but got 3 channels instead

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpv7h3brzf/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpv7h3brzf/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpv7h3brzf', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv_transpose = torch.nn.ConvTranspose1d(6, 2, 3, stride=2)

    def forward(self, x1, x2):
        v1 = torch.tanh(x1 * x2) + torch.sigmoid(x1 * x2)
        v2 = self.conv_transpose(v1)
        v3 = torch.sigmoid(v2)
        v4 = torch.sigmoid(x1 * x2) + torch.tanh(x1 * x2)
        v5 = torch.tanh(v4)
        v6 = torch.tanh(v5 * v6) + torch.sigmoid(v4 * v6)
        v7 = v1 - v2
        v8 = v1 * v3
        return v7 * v8



func = Model().to('cpu')


x1 = torch.randn(1, 6, 28)

x2 = torch.randn(1, 6, 28)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
local variable 'v6' referenced before assignment

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp3t4wljot/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp3t4wljot/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp3t4wljot', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 6, 4, stride=3, padding=2, groups=1, bias=True)
        self.relu = torch.nn.ReLU()
        self.hardswish = torch.nn.Hardswish()
        self.elu = torch.nn.ELU(0.75)
        self.selu = torch.nn.SELU(0.75)
        self.gelu = torch.nn.GELU()

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.tanh(v1)
        v3 = self.relu(v1)
        v4 = self.hardswish(v1)
        v5 = self.elu(v1)
        v6 = self.selu(v1)
        v7 = self.gelu(v1)
        v8 = v2 + v3
        v9 = v4 + v5
        v10 = v6 + v7
        v11 = v8 + v9
        v12 = v10 + v11
        return v10



func = Model().to('cpu')


x1 = torch.randn(2, 1, 3, 3)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpw_369i9h/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpw_369i9h/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpw_369i9h', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
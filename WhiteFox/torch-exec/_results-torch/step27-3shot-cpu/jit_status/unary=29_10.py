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

    def __init__(self, min_value=0.43, max_value=1.76):
        super().__init__()
        self.gelu = torch.nn.GELU()
        self.conv_transpose3d = torch.nn.ConvTranspose3d(8, 12, (1, 3, 3), stride=1, padding=0)
        self.tanh = torch.nn.Tanh()
        self.act_11 = torch.nn.ReLU()
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.gelu(x1)
        v2 = self.conv_transpose3d(v1)
        v3 = self.tanh(v2)
        v4 = self.act_11(v3)
        v5 = (self.max_value + 0.031970393009503294) * v4
        v6 = torch.clamp_min(v5, self.min_value)
        v7 = torch.clamp_max(v6, self.max_value)
        return v7



func = Model().to('cpu')


x1 = torch.randn(1, 8, 64, 64, 64)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpb4phxga9/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpb4phxga9/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpb4phxga9', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
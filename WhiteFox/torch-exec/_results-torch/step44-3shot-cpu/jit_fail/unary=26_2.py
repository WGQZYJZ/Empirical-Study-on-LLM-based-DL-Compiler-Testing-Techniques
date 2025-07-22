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
        self.linear = torch.nn.Linear(57, 44, bias=False)
        self.conv_t = torch.nn.ConvTranspose1d(44, 19, 5, padding=0, bias=False)

    def forward(self, x4):
        m1 = self.linear(x4)
        m2 = self.conv_t(m1).clamp(min=0) * 0.089302203 + 0.37970184
        return torch.sigmoid(m2)



func = Model().to('cpu')


x4 = torch.randn(6, 57, device='cuda')

test_inputs = [x4]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [44, 19, 5], expected input[1, 6, 44] to have 44 channels, but got 6 channels instead

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp9x6st1rw/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp9x6st1rw/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp9x6st1rw', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
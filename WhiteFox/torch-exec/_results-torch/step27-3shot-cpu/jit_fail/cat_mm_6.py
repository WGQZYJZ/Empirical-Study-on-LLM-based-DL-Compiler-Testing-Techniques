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

    def forward(self, x1, x2):
        x1 = torch.randn_like(x2).transpose(-1, -2).contiguous()
        v1 = torch.nn.functional.interpolate(x1, mode='nearest', scale_factor=2) * (1.0 / torch.sqrt(2))
        v2 = torch.nn.functional.interpolate(x1, mode='nearest', scale_factor=0.1) * (1.0 / torch.sqrt(2))
        return torch.cat([v1, v1, v2, v2], 2).contiguous()



func = Model().to('cpu')


x1 = torch.randn(2, 2, 2)

x2 = torch.randn(2, 2, 2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
sqrt(): argument 'input' (position 1) must be Tensor, not int

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmplrz_keyv/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmplrz_keyv/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmplrz_keyv', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
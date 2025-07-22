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

    def forward(self, v0, v2, v3, v4, v7):
        v5 = torch.mm(v3, v7)
        v1 = torch.mm(v5, v7)
        v9 = torch.mm(v0, v7)
        v8 = torch.mm(v9, v3)
        v6 = torch.mm(v8, v5)
        v10 = torch.mm(v3, v5)
        return v2 * v6 * v1 * v10



func = Model().to('cpu')


v0 = torch.randn(8, 8)

v2 = torch.randn(8, 8)

v3 = torch.randn(8, 8)

v4 = torch.randn(8, 8)

v7 = torch.randn(8, 8)

test_inputs = [v0, v2, v3, v4, v7]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp74qbzq3m/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp74qbzq3m/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp74qbzq3m', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
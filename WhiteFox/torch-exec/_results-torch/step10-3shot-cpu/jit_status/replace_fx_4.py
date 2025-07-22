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

    def forward(self, a, b, c):
        y = torch.nn.functional.dropout(b, p=0.5)
        x = torch.nn.functional.gelu(c)
        v1 = torch.rand_like(a, dtype=torch.float)
        w1 = torch.rand_like(b, dtype=torch.float)
        y = y + x
        x = torch.nn.functional.sigmoid(y)
        t = torch.nn.functional.silu(x)
        a = t + v1
        return a



func = Model().to('cpu')


a = torch.randn(2, 2, 10)

b = torch.randn(2, 2, 10)

c = torch.randn(2, 2, 10)

test_inputs = [a, b, c]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmprmv7ggie/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmprmv7ggie/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmprmv7ggie', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

class Module(torch.nn.Module):

    def forward(self, a, b):
        t = a + b - 1
        t1 = torch.nn.functional.gelu(t * 0.0709)
        t2 = torch.nn.functional.relu(t)
        t3 = torch.log(t)
        t4 = torch.sigmoid(t)
        t5 = torch.sqrt(t)
        t6 = torch.pow(t4, 0.418)
        t7 = torch.nn.functional.gelu(t, approximate=True)
        t8 = torch.nn.functional.gelu(t, approximate=False)
        t9 = torch.nn.functional.silu(t)
        t10 = t7 - t8
        t11 = torch.nn.functional.silu(t - t9)
        t12 = torch.tanh(t)
        t13 = torch.nn.functional.softplus(t)
        m = t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t9 + t10 + t11 + t12 + t13
        t14 = m
        return t14



func = Module().to('cpu')


A = torch.randn(3, 4)

B = torch.randn(3, 4)

test_inputs = [A, B]

# JIT_FAIL
'''
direct:
gelu(): argument 'approximate' must be str, not bool

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpy8wkud11/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpy8wkud11/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpy8wkud11', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
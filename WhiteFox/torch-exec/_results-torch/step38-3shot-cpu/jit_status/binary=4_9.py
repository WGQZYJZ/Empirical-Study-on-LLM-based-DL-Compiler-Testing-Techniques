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

class Module1(torch.nn.Module):

    def __init__(self, dim, bias):
        super().__init__()
        self.linear = torch.nn.Linear(dim, dim, bias=bias)

    def forward(self, x):
        v2 = self.linear(x)
        return v2

class Model(torch.nn.Module):

    def __init__(self, num_features):
        super().__init__()
        self.module1 = Module1(num_features, False)
        self.module2 = Module1(num_features, True)

    def forward(self, x):
        v1 = self.module1(x)
        v2 = self.module2(x)
        res = v2 + v1
        return res


num_features = 32
func = Model(num_features).to('cpu')


num_features = 32
x = torch.randn(2, num_features)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpdma_fmad/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpdma_fmad/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpdma_fmad', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.linear1 = torch.nn.Linear(15, 32, bias=False)
        self.linear2 = torch.nn.Linear(32, 2, bias=False)

    def forward(self, x):
        v1 = self.linear1(x)
        v2 = v1 * 0.5
        v3 = self.linear1(x)
        v4 = v3 * v3
        v5 = v4 * v4
        v6 = v5 * 0.044715
        v7 = self.linear1(x) * v6
        v8 = v7 * 0.7978845608028654
        v9 = v8 + 1
        v10 = torch.tanh(v9)
        v11 = v7 + v10
        v12 = v2 * v11
        return v12


func = Model().to('cpu')


x = torch.randn(1, 15)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp18_9_cqh/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp18_9_cqh/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp18_9_cqh', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
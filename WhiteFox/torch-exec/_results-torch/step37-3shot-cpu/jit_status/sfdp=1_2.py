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
        self.proj_q = torch.nn.Linear(3072, 4096)
        self.proj_k = torch.nn.Linear(3072, 4096)
        self.proj_v = torch.nn.Linear(3072, 4096)

    def forward(self, x1, x2):
        v1 = self.proj_q(x1)
        v2 = self.proj_k(x2)
        v3 = self.proj_v(x2)
        v4 = torch.matmul(v1, v2.transpose(-2, -1))
        v5 = v4.div(2048.0)
        v6 = v5.softmax(dim=-1)
        v7 = torch.nn.functional.dropout(v6, 0.1)
        v8 = torch.matmul(v7, v3)
        return v8


func = Model().to('cpu')


x1 = torch.randn(1, 3072)

x2 = torch.randn(1, 3072)

test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpd62c1pqj/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpd62c1pqj/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpd62c1pqj', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.query = torch.nn.Linear(64, 128)
        self.key = torch.nn.Linear(64, 128)
        self.value = torch.nn.Linear(64, 128)

    def forward(self, Q, K, V):
        v1 = self.query(Q)
        v2 = self.key(K)
        v3 = self.value(V)
        v4 = torch.matmul(v1, v2.transpose(-2, -1))
        v5 = v4.div(16)
        v6 = torch.nn.functional.softmax(v5, dim=-1)
        v7 = 0.1 * v6
        v8 = torch.matmul(v7, v3)
        return v8


func = Model().to('cpu')

device = torch.device('cpu')

x1 = torch.randn(1, 64, device=device)
device = torch.device('cpu')

x2 = torch.randn(1, 64, device=device)
device = torch.device('cpu')

x3 = torch.randn(1, 64, device=device)

test_inputs = [x1, x2, x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpbfozm6nd/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpbfozm6nd/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpbfozm6nd', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
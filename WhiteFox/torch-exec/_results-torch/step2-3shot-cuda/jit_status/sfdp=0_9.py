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
        self.linear = torch.nn.Linear(25, 10)
        self.key = torch.nn.Linear(10, 10)
        self.query = torch.nn.Linear(10, 10)
        self.value = torch.nn.Linear(10, 10)

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = self.linear(x2)
        v3 = v1 + v2
        v4 = self.key(v3)
        v5 = self.query(v3)
        v6 = self.value(v3)
        v7 = torch.matmul(v4, v5.transpose(-2, -1))
        v8 = torch.nn.functional.softmax(v7, dim=-1)
        v9 = torch.matmul(v8, v6)
        return v9


func = Model().to('cuda')


x1 = torch.randn(1, 25)

x2 = torch.randn(1, 25)

test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpucslfy2m/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpucslfy2m/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpucslfy2m', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
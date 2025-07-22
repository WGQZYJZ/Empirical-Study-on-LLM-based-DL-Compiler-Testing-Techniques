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

    def __init__(self, input_dim, hidden_dim):
        super().__init__()
        self.query = torch.nn.Linear(input_dim, hidden_dim)
        self.key = torch.nn.Linear(input_dim, hidden_dim)
        self.value = torch.nn.Linear(input_dim, hidden_dim)

    def forward(self, query, key, value, scale_factor, dropout_p):
        v1 = self.query(query)
        v2 = self.key(key)
        v3 = self.value(value)
        v4 = torch.matmul(v1, v2.transpose(-2, -1))
        v5 = v4.div(scale_factor)
        v6 = torch.nn.functional.dropout(v5, p=dropout_p)
        v7 = torch.matmul(v6, v3)
        return v7


input_dim = 1
hidden_dim = 1
func = Model(32, 64).to('cpu')


q = torch.randn(4, 8, 32)

k = torch.randn(4, 16, 32)

v = torch.randn(4, 16, 32)

scale_factor = torch.randn(1)
query = 1

test_inputs = [q, k, v, scale_factor, query]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp2q93njqg/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp2q93njqg/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp2q93njqg', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
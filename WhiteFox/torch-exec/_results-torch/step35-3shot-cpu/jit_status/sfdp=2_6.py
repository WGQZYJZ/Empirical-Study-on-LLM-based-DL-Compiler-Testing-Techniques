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

    def __init__(self, d_query, d_key, d_value, dropout_p=0.2):
        super().__init__()
        self.query = torch.nn.Parameter(torch.empty(d_query))
        self.key = torch.nn.Parameter(torch.empty(d_key))
        self.value = torch.nn.Parameter(torch.empty(d_value))
        self.scale_factor = 1.0 / np.sqrt(d_query)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value):
        out = torch.matmul(query, key.transpose(-2, -1))
        out = out * self.scale_factor
        out = out.softmax(dim=-1)
        out = self.dropout(out)
        out = torch.matmul(out, value)
        return out


d_query = 1
d_key = 1
d_value = 1
func = Model(256, 256, 256).to('cpu')


query = torch.randn(16, 256)

key = torch.randn(16, 256)

value = torch.randn(16, 256)

test_inputs = [query, key, value]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpjhp36pam/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpjhp36pam/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpjhp36pam', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
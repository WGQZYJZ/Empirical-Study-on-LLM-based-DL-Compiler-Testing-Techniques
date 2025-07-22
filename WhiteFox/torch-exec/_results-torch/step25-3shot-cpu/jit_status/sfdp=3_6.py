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

    def __init__(self, num_heads, dim_qk, dim_v, dropout_p, scale_factor=1.0):
        super().__init__()
        self.num_heads = num_heads
        self.dim_qk = dim_qk
        self.dim_v = dim_v
        self.dropout_p = dropout_p
        self.scale_factor = scale_factor
        self.project_q = torch.nn.Linear(self.dim_qk, self.num_heads * self.dim_qk)
        self.project_k = torch.nn.Linear(self.dim_qk, self.num_heads * self.dim_qk)
        self.project_v = torch.nn.Linear(self.dim_v, self.num_heads * self.dim_v)

    def forward(self, query, key, value):
        q = self.project_q(query).chunk(self.num_heads, dim=-1)
        k = self.project_k(key).chunk(self.num_heads, dim=-1)
        v = self.project_v(value).chunk(self.num_heads, dim=-1)
        q = torch.cat(q, dim=0)
        k = torch.cat(k, dim=0)
        v = torch.cat(v, dim=0)
        q = q.reshape_as(k)
        k = k.reshape_as(v)
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
        return output


num_heads = 2
dim_qk = 10
dim_v = 10
dropout_p = 0.1
func = Model(num_heads, dim_qk, dim_v, dropout_p).to('cpu')


dim_qk = 10
num_heads = 2
query = torch.randn(4, 2, num_heads, dim_qk)

dim_qk = 10
num_heads = 2
key = torch.randn(4, 2, num_heads, dim_qk)

dim_v = 10
num_heads = 2
value = torch.randn(4, 2, num_heads, dim_v)

test_inputs = [query, key, value]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp1hu_ni3r/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp1hu_ni3r/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp1hu_ni3r', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
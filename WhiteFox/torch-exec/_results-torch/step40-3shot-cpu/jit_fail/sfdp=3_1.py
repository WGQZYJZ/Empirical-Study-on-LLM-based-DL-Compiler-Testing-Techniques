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

    def __init__(self, embed_dim, num_heads, dropout_p):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.dropout_p = dropout_p
        self.head_dim = embed_dim // num_heads
        self.linear_q = torch.nn.Linear(embed_dim, embed_dim)
        self.linear_k = torch.nn.Linear(embed_dim, embed_dim)
        self.linear_v = torch.nn.Linear(embed_dim, embed_dim)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value):
        q = self.linear_q(query)
        k = self.linear_k(key)
        v = self.linear_v(value)
        q = q.view(q.shape[0], q.shape[1], self.num_heads, self.head_dim).permute(0, 2, 1, 3)
        k = k.view(k.shape[0], k.shape[1], self.num_heads, self.head_dim).permute(0, 2, 1, 3)
        v = v.view(v.shape[0], v.shape[1], self.num_heads, self.head_dim).permute(0, 2, 1, 3)
        scaled_qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = scaled_qk * self.head_dim ** (-0.5)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        output = torch.matmul(dropout_qk, v).permute(0, 2, 1, 3).contiguous()
        return output.view(output.shape[0], output.shape[1], self.embed_dim)


embed_dim = 1
num_heads = 1
dropout_p = 1
func = Model(32, 8, 0.5).to('cpu')


x1 = torch.randn(64, 8, 32)

x2 = torch.randn(64, 8, 32)
query = 1

test_inputs = [x1, x2, query]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpb7ntxxb2/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpb7ntxxb2/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpb7ntxxb2', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
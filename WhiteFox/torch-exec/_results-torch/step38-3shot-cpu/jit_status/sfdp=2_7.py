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

    def __init__(self, num_heads, hidden_dim):
        super().__init__()
        self.key = torch.nn.Linear(hidden_dim, hidden_dim)
        self.query = torch.nn.Linear(hidden_dim, hidden_dim)

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, dropout_p)
        output = dropout_qk.matmul(value)
        return output


num_heads = 2
hidden_dim = 16
func = Model(num_heads, hidden_dim).to('cpu')

num_heads = 2
hidden_dim = 16

query = torch.randn(1, hidden_dim * num_heads, 8, 64)
num_heads = 2
hidden_dim = 16

key = torch.randn(1, hidden_dim * num_heads, 8, 64)
num_heads = 2
hidden_dim = 16

value = torch.randn(1, hidden_dim * num_heads, 8, 64)
inv_scale_factor = 1
dropout_p = 1

test_inputs = [query, key, value, inv_scale_factor, dropout_p]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp0zfqhmdr/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp0zfqhmdr/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp0zfqhmdr', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
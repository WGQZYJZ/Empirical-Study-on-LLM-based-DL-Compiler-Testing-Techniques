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

    def __init__(self, d_model, num_heads, hidden_dim):
        super().__init__()
        self.query_linear = torch.nn.Linear(hidden_dim, d_model)
        self.key_linear = torch.nn.Linear(hidden_dim, d_model)

    def attention(self, query, key, value, mask=None):
        k = self.key_linear(key)
        q = self.query_linear(query)
        qk = q @ k.transpose(-2, -1)
        qk = qk / math.sqrt(q.size(-1))
        if mask is not None:
            qk += mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output

    def forward(self, x1, x2):
        v1 = self.attention(x1, x2, x2)
        return v1


d_model = 512
num_heads = 1
hidden_dim = 2048
func = Model(d_model, 8, hidden_dim).to('cpu')


x1 = torch.randn(1, 8, 64, 2048)

x2 = torch.randn(1, 8, 256, 2048)

test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp8t3w2h8x/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp8t3w2h8x/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp8t3w2h8x', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
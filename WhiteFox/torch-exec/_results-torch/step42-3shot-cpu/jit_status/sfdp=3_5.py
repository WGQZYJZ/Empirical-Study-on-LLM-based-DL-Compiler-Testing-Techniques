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

    def __init__(self, dim, num_heads, dropout_p):
        super().__init__()
        self.dim = dim
        self.num_heads = num_heads
        self.dropout_p = dropout_p
        self.dim_per_head = dim // num_heads
        self.sqrt_dim_per_head = math.sqrt(self.dim_per_head)
        self.query = Parameter(torch.Tensor(dim, dim))
        self.key = Parameter(torch.Tensor(dim, dim))
        self.value = Parameter(torch.Tensor(dim, dim))
        self.softmax_scale = math.sqrt(math.sqrt(dim))
        self.dropout = nn.Dropout(dropout_p)

    def forward(self, x1, x2):
        q = x1.matmul(self.query.div_(self.sqrt_dim_per_head))
        k = x2.matmul(self.key.div_(self.sqrt_dim_per_head)).transpose(-2, -1)
        k = self.softmax_scale * k
        v = x2.matmul(self.value.div_(self.sqrt_dim_per_head))
        qktv = q.matmul(k).matmul(v)
        result = self.dropout(qktv)
        return result


dim = 1
num_heads = 1
dropout_p = 1
func = Model(3072, 2, 0.1).to('cpu')


x1 = torch.randn(20, 25, 3072)

x2 = torch.randn(20, 25, 3072)

test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmphdbhtwgi/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmphdbhtwgi/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmphdbhtwgi', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.dim = 96
        self.num_heads = 16
        self.scaling = self.dim ** (-0.5)
        self.query_projection = torch.nn.Linear(self.dim, self.dim)
        self.key_projection = torch.nn.Linear(self.dim, self.dim)
        self.value_projection = torch.nn.Linear(self.dim, self.dim)

    def forward(self, query, key, value):
        query = self.query_projection(query)
        key = self.key_projection(key)
        value = self.value_projection(value)
        inv_scale = self.scaling / query.shape[0] ** 0.5
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) * inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


func = Model().to('cuda')


query = torch.randn(1, 1, 96)

key = torch.randn(1, 1, 96)

value = torch.randn(1, 1, 96)

test_inputs = [query, key, value]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp10laco62/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp10laco62/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp10laco62', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
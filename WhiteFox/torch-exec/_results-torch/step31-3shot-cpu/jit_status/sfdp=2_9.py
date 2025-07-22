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

    def __init__(self, dim):
        super().__init__()
        self.dim = dim
        self.proj = torch.nn.Linear(dim, dim)

    def forward(self, query, key, value):
        q = self.proj(query).view(query.size(0), query.size(1), 1, self.dim)
        k = self.proj(key).view(key.size(0), 1, -1, self.dim)
        res = torch.matmul(q, k.transpose(-2, -1))
        res = res / math.sqrt(self.dim)
        res = torch.nn.functional.softmax(res, dim=-1)
        res = torch.nn.functional.dropout(res, p=0.5)
        res = torch.matmul(res, value)
        return res


dim = 1
func = Model(512).to('cpu')


query = torch.randn(1, 2, 512)

key = torch.randn(1, 2, 512)

value = torch.randn(1, 2, 512)

test_inputs = [query, key, value]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpvag3t94d/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpvag3t94d/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpvag3t94d', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
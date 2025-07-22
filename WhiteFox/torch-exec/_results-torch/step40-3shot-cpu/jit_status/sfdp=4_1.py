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

    def forward(self, q, k, v, mask):
        qk = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        qk = qk + mask
        attn_mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v
        return output

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, q, k2, v2, mask):
        qk = q @ k2.transpose(-2, -1) / math.sqrt(q.size(-1))
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v2
        return output

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x5, q5, k, v, mask):
        qk = x5 @ k.transpose(-2, -1) / math.sqrt(x5.size(-1))
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v
        return output

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x2, k, v, mask):
        qk = x2 @ k.transpose(-2, -1) / math.sqrt(x2.size(-1))
        qk = qk + mask
        attn_mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v
        return output

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x5, n5, k, v, mask):
        qk = x5 @ k.transpose(-2, -1) / math.sqrt(x5.size(-1))
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v
        return output

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, k2, v2, q, mask):
        qk = q @ k2.transpose(-2, -1) / math.sqrt(q.size(-1))
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v2
        return output



func = Model().to('cpu')


Q = torch.randn(1, 64, 56, 56)

K = torch.randn(1, 64, 56, 56)

V = torch.randn(1, 64, 56, 56)

mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)

test_inputs = [Q, K, V, mask]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_14c1f79/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp_14c1f79/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp_14c1f79', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
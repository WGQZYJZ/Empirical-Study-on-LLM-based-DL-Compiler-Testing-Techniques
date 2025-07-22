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
        self.emb_dim = 32
        self.head = 8
        self.num_patch = int(8 * 8 + 4 * 4 + 2 * 2 + 1)
        self.pos_dim = self.emb_dim // self.head
        self.query_emb = torch.nn.Embedding(self.num_patch + 1, self.emb_dim)
        self.key_emb = torch.nn.Embedding(self.num_patch + 1, self.emb_dim)
        self.value_emb = torch.nn.Identity()

    def forward(self, x0):
        v0 = torch.arange(x0.shape[1])
        v1 = v0.unsqueeze(0)
        v2 = v1.unsqueeze(-1)
        v3 = v0.unsqueeze(-1)
        v4 = v3 + v2
        v5 = v4.reshape(-1)
        q = self.query_emb(v5)
        k = self.key_emb(v5)
        v = self.value_emb(v5)
        v6 = q @ k.transpose(-2, -1)
        v7 = v6 / self.pos_dim ** 0.5
        v8 = F.softmax(v7, dim=-1)
        v9 = F.dropout(v8, 0.0)
        d_v9 = v9 @ v
        return d_v9


func = Model().to('cpu')


x0 = torch.tensor([[1], [4], [7], [2], [-2], [6], [3], [5]])

test_inputs = [x0]

# JIT_FAIL
'''
direct:
expected scalar type Float but found Long

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp3ysj8wtw/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp3ysj8wtw/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp3ysj8wtw', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
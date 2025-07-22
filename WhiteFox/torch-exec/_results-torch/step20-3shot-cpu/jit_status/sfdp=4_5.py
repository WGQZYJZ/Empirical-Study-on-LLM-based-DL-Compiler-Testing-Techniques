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

    def forward(self, q, k, v):
        qk = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        attn_mask = qk.new_ones(qk.size())
        attn_mask = torch.triu(attn_mask, diagonal=1)
        attn_mask = 1.0 / attn_mask
        attn_mask = attn_mask.masked_fill(attn_mask == 0, -10000.0)
        return (qk * attn_mask, attn_mask)


func = Model().to('cpu')


q = torch.randn(1, 2, 3, 4)

k = torch.randn(1, 2, 3, 4)

v = torch.randn(1, 2, 5, 4)

test_inputs = [q, k, v]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_oahdybv/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp_oahdybv/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp_oahdybv', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
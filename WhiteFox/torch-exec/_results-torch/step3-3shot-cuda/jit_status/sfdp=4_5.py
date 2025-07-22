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
        self.query = torch.nn.Linear(8, 8, bias=True)
        self.key = torch.nn.Linear(8, 8, bias=True)
        self.value = torch.nn.Linear(8, 8, bias=True)

    def forward(self, query, key, value, attn_mask=None):
        q = self.query(query)
        k = self.key(key)
        v = self.value(value)
        k = torch.transpose(k, -2, -1)
        qk = q @ k
        qk = qk / math.sqrt(q.size(-1))
        if attn_mask != None:
            qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v
        return output


func = Model().to('cuda')


query = torch.randn(8, 10, 8)

key = torch.randn(8, 20, 8)

value = torch.randn(8, 20, 8)

test_inputs = [query, key, value]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpl_wwshnj/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpl_wwshnj/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpl_wwshnj', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
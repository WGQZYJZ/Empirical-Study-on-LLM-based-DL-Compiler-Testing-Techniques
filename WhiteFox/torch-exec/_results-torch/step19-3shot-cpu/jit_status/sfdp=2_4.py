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
        self.qkv = torch.nn.Linear(4, 8)
        self.dropout = torch.nn.Dropout(0.25)

    def forward(self, queries, keys, values):
        qkv = self.qkv(queries).chunk(3, dim=-1)
        (q, k, v) = [e.squeeze(dim=0) for e in qkv]
        qkv = torch.matmul(q, k.transpose(-2, -1))
        scaled_qkv = qkv.div(100)
        softmax_qkv = scaled_qkv.softmax(dim=-1)
        dout_qkv = self.dropout(softmax_qkv)
        output = torch.matmul(dout_qkv, v)
        return output


func = Model().to('cpu')


queries = torch.randn(1, 5, 4)

keys = torch.randn(4, 6, 4)

values = torch.randn(4, 6, 8)

test_inputs = [queries, keys, values]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpk4oy21qm/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpk4oy21qm/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpk4oy21qm', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
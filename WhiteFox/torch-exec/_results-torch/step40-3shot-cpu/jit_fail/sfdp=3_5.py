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

    def forward(query, key, value, scale_factor, dropout_p):
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v2 = v1 * scale_factor
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)
        output = v4.matmul(value)
        return output



func = Model().to('cpu')


dim_size = 128 + 128
seq_len = 3
batch_size = 1
query = torch.randn(batch_size, seq_len, dim_size)

dim_size = 128 + 128
seq_len = 3
batch_size = 1
key = torch.randn(batch_size, seq_len, dim_size)

dim_size = 128 + 128
seq_len = 3
batch_size = 1
value = torch.randn(batch_size, seq_len, dim_size)


scale_factor = torch.sigmoid(torch.randn(1))

test_inputs = [query, key, value, scale_factor]

# JIT_FAIL
'''
direct:
matmul(): argument 'input' (position 1) must be Tensor, not Model

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpd2q5n66q/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpd2q5n66q/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpd2q5n66q', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
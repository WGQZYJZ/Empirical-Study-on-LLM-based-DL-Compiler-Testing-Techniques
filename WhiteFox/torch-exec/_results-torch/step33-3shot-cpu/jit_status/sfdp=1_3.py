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

    def __init__(self, num_heads, query_size, key_size, hidden_size, dropout_p):
        super().__init__()
        self.scale_factor = torch.sqrt(torch.tensor([key_size]).float())
        self.query = torch.nn.Linear(query_size, hidden_size)
        self.key = torch.nn.Linear(key_size, hidden_size)
        self.value = torch.nn.Linear(key_size, hidden_size)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, query, key, value, dropout_p=0.0):
        q = self.query(query)
        k = self.key(key)
        v = self.value(value)
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_output = self.dropout(softmax_qk)
        output = dropout_output.matmul(v)
        return (output, softmax_qk)


num_heads = 1
query_size = 1
key_size = 1
hidden_size = 1
dropout_p = 0.0
func = Model(12, 32, 32, 64, 0.0).to('cpu')


query = torch.randn(2, 12, 32)

key = torch.randn(2, 12, 32)

value = torch.randn(2, 12, 32)

test_inputs = [query, key, value]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpf70fkeo3/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpf70fkeo3/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpf70fkeo3', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
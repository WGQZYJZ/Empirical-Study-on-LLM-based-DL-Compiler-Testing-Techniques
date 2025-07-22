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

    def __init__(self, query_len, key_len, value_len, hidden_size, scale_factor, dropout_p):
        super().__init__()

    def forward(self, query, key, value, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


query_len = 500
key_len = 400
value_len = 400
hidden_size = 128
scale_factor = 1 / hidden_size ** 0.5
dropout_p = 0.5
func = Model(query_len, key_len, value_len, hidden_size, scale_factor, dropout_p).to('cpu')


hidden_size = 128
query_len = 500
query = torch.randn(1, query_len, hidden_size)

hidden_size = 128
key_len = 400
key = torch.randn(1, key_len, hidden_size)

hidden_size = 128
value_len = 400
value = torch.randn(1, value_len, hidden_size)
dropout_p = 1

test_inputs = [query, key, value, dropout_p]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmped7kkvv5/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmped7kkvv5/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmped7kkvv5', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
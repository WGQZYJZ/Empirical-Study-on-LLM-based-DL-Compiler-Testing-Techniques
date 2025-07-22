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

    def __init__(self, dim_model):
        super().__init__()
        self.dim_model = dim_model

    def forward(self, query, key, value, scale_factor, dropout_p):
        key = key.transpose(-2, -1)
        qk = torch.matmul(query, key)
        scaled_qk = qk.div(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output

    def init_weight(self):
        for weight in self.parameters():
            nn.init.trunc_normal_(weight.data, std=0.02)


dim_model = 32
func = Model(dim_model).to('cpu')


dim_model = 32
query = torch.randn(2, 10, dim_model)

dim_model = 32
key = torch.randn(2, 15, dim_model)

dim_model = 32
value = torch.randn(2, 15, dim_model)
scale_factor = 1
dropout_p = 1

test_inputs = [query, key, value, scale_factor, dropout_p]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_11pz3b5/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp_11pz3b5/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp_11pz3b5', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
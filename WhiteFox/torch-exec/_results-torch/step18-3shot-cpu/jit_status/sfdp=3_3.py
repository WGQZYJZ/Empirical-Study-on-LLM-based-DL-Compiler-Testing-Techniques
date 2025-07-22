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

    def __init__(self, num_heads=8, d_model=26, dropout_rate=0.0):
        super().__init__()
        self.attn_qk = torch.nn.Linear(d_model, num_heads)
        self.v = torch.nn.Linear(d_model, d_model)
        self.dropout = torch.nn.Dropout(dropout_rate)

    def forward(self, query, key, value):
        qk = self.attn_qk(query) * self.attn_qk(key)
        scale_factor = torch.sqrt(torch.Tensor([query.shape[-1]]))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        output = self.v(dropout_qk.matmul(value))
        return output


func = Model(num_heads=2, d_model=4, dropout_rate=0.0).to('cpu')


query = torch.randn(2, 4)

key = torch.randn(2, 4)

value = torch.randn(2, 4)

test_inputs = [query, key, value]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp3ques420/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp3ques420/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp3ques420', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
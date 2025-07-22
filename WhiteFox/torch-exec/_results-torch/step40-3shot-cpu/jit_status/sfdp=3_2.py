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

    def __init__(self, d_model, n_heads, dropout_p):
        super().__init__()
        self.dropout_p = dropout_p
        self.query_proj = torch.nn.Linear(d_model, d_model)
        self.key_proj = torch.nn.Linear(d_model, d_model)
        self.value_proj = torch.nn.Linear(d_model, d_model)
        self.scaled_proj = torch.nn.Parameter(torch.Tensor([0.0]))

    def forward(self, x1):
        q = self.query_proj(x1)
        k = self.key_proj(x1)
        v = self.value_proj(x1)
        scale_factor = self.scaled_proj.exp()
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
        return output


d_model = 1
n_heads = 1
dropout_p = 1
func = Model(128, 4, 0.1).to('cpu')


x1 = torch.randn(1, 64, 128)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpcvbk947g/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpcvbk947g/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpcvbk947g', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
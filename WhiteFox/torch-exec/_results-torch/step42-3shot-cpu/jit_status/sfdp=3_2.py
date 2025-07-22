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
        self.head_dim = 64

    def forward(self, q, k, v):
        query = q.reshape(-1, 1, 1, self.head_dim)
        key = k.reshape(-1, 1, 1, self.head_dim)
        value = v.reshape(-1, 1, 1, self.head_dim)
        softmax_qk = torch.matmul(query, key.transpose(-2, -1))
        scale_factor = softmax_qk.size(-1) ** (-0.5)
        softmax_qk = softmax_qk * scale_factor
        softmax_qk = torch.nn.functional.softmax(softmax_qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = dropout_qk.matmul(value)
        return output.reshape(-1, 1024)


func = Model().to('cpu')


q = torch.randn(1, 1, 1, 1024)

k = torch.randn(1, 1, 1, 1024)

v = torch.randn(1, 1, 1, 1024)

test_inputs = [q, k, v]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmplszicpn7/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmplszicpn7/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmplszicpn7', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
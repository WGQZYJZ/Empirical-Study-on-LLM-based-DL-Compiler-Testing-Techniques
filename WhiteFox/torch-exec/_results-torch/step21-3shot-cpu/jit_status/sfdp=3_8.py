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

    def __init__(self, key_size, dropout_p):
        super().__init__()
        self.scale_factor = 1.0 / math.sqrt(key_size)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, q, k, v):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = self.scale_factor * qk
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        return dropout_qk.matmul(v)


key_size = 1
dropout_p = 1

func = Model(key_size, dropout_p).to('cpu')


q = torch.randn(5, 4, 200)

k = torch.randn(5, 6, 200)

v = torch.randn(5, 6, 100)

test_inputs = [q, k, v]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp861g4btw/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp861g4btw/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp861g4btw', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def __init__(self, dropout_p=0.0):
        super().__init__()
        self.dropout_p = dropout_p

    def forward(self, query, key, value, attn_mask):
        qk = torch.matmul(query, key.transpose(-2, -1))
        qk = torch.nn.functional.dropout(qk, self.dropout_p)
        qk = qk.softmax()
        dropout_qk = torch.matmul(value, qk)
        return dropout_qk


func = Model(dropout_p=0.5).to('cpu')


query = torch.randn(1, 8, 64)

key = torch.randn(1, 8, 64)

value = torch.randn(1, 8, 64)

attn_mask = torch.randn(1, 1, 64)

test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
softmax() received an invalid combination of arguments - got (), but expected one of:
 * (int dim, torch.dtype dtype = None)
 * (name dim, *, torch.dtype dtype = None)


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_p9n6wj5/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp_p9n6wj5/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp_p9n6wj5', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
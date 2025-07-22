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

    def __init__(self, dim):
        super().__init__()
        self.dim = dim

    def forward(self, q, k, v, scale_factor=None, dropout_p=0.0):
        q_k = torch.matmul(q, k.transpose(-2, -1))
        if scale_factor is not None:
            q_k = q_k.div(scale_factor)
        softmax_qk = torch.nn.functional.softmax(q_k, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1, training=self.training)
        output = dropout_qk.matmul(v)
        return output


dim = 1
func = Model(2).to('cpu')


q = torch.randn(1, 5, 2)

k = torch.randn(1, 6, 2)

v = torch.randn(1, 6, 2)

test_inputs = [q, k, v]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_yo53996/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp_yo53996/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp_yo53996', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
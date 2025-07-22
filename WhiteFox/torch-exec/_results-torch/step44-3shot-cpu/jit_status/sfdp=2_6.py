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

    def forward(self, x1, x2, x3, x4):
        q = x1
        k = x2
        v = x3
        s = x4
        c = q.size(-1)
        kq = torch.matmul(q, k.transpose(-2, -1))
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(s)
        softmax = scaled_qk.softmax(dim=-1)
        dropout = torch.nn.functional.dropout(softmax, p=0.009)
        output = dropout.matmul(v)
        return output


func = Model().to('cpu')


q = torch.randn(2, 512, 80)

k = torch.randn(2, 512, 80)

v = torch.randn(2, 512, 512)

s = torch.randn(1)

test_inputs = [q, k, v, s]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpesvr9wpl/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpesvr9wpl/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpesvr9wpl', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
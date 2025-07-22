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

    def forward(self, q1, k1, v1):
        qk = torch.matmul(q1, k1.transpose(-2, -1))
        scaled_qk = qk.div(2 ** 0.5)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.2)
        output = dropout_qk.matmul(v1)
        return output


func = Model().to('cuda')


q1 = torch.randn(1, 8, 32, 32)

k1 = torch.randn(1, 8, 32, 32)

v1 = torch.randn(1, 8, 32, 32)

test_inputs = [q1, k1, v1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_4xddkok/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp_4xddkok/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp_4xddkok', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
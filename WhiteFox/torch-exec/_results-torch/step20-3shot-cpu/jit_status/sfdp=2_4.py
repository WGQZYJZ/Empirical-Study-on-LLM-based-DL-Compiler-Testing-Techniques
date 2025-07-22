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

    def forward(self, Q, K, V, dropout_p, inv_scale_factor):
        Q = Q.transpose(0, 1)
        K = K.transpose(0, 1)
        Kt = K.transpose(-2, -1)
        QK = torch.matmul(Q, Kt)
        scaled_QK = QK.div(inv_scale_factor)
        softmax_QK = F.softmax(scaled_QK, dim=-1)
        dropout_QK = F.dropout(softmax_QK, p=dropout_p)
        output = torch.matmul(dropout_QK, V.transpose(0, 1))
        return output


func = Model().to('cpu')


Q = torch.randn(16, 1, 1024)

K = torch.randn(16, 1, 1024)

V = torch.randn(16, 1, 1024)
dropout_p = 1
inv_scale_factor = 1

test_inputs = [Q, K, V, dropout_p, inv_scale_factor]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp8o2yyfy7/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp8o2yyfy7/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp8o2yyfy7', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
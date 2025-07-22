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

    def forward(self, q1, k1, v1, inv_scale_factor, dropout_p, dropout_m, dropout_inplace):
        qk = torch.matmul(q1, k1.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        if dropout_m is None:
            dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p, inplace=dropout_inplace)
        else:
            dropout_qk_mask = torch.nn.functional.dropout(torch.ones_like(softmax_qk), p=dropout_p, inplace=dropout_inplace)
            dropout_qk = softmax_qk.mul(dropout_qk_mask).div(1.0 - dropout_m)
        return dropout_qk.matmul(v1)


func = Model().to('cpu')


q1 = torch.randn(1, 8, 5)

k1 = torch.randn(1, 6, 5)

v1 = torch.randn(1, 6, 5)

inv_scale_factor = torch.tensor(1e-05)
dropout_p = 1
dropout_m = 1
dropout_inplace = 1

test_inputs = [q1, k1, v1, inv_scale_factor, dropout_p, dropout_m, dropout_inplace]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpmyfj44bk/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpmyfj44bk/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpmyfj44bk', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
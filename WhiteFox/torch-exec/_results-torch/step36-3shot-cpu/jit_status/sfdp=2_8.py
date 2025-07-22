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

    def forward(self, q, k, v):
        _qk = torch.matmul(q, k.transpose(-2, -1))
        __inv_scale_factor__ = math.sqrt(k.shape[-1])
        __dropout_p__ = 0.9
        dropout_qk = torch.nn.functional.dropout(_qk / __inv_scale_factor__, p=__dropout_p__)
        output = torch.matmul(dropout_qk, v)
        return output


func = Model().to('cpu')


q = torch.randn(2, 8, 16)

k = torch.randn(2, 4, 16)

v = torch.randn(2, 4, 8)

test_inputs = [q, k, v]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpsrepceg5/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpsrepceg5/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpsrepceg5', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
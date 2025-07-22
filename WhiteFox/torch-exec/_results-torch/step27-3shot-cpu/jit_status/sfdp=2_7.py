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
        self.inv_scale_factor = 1.0 / math.sqrt(832)

    def forward(self, queries, keys, values, mask, dropout):
        qk = torch.matmul(queries, keys.transpose(-2, -1)) * self.inv_scale_factor
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout)
        output = dropout_qk.matmul(values).mean(dim=1)
        return output


func = Model().to('cpu')


queries = torch.randn(1, 2048, 768)

keys = torch.randn(1, 10, 2048, 768)

values = torch.randn(1, 10, 2048, 768)
mask = 1
dropout = 1

test_inputs = [queries, keys, values, mask, dropout]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmptuj_y2r6/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmptuj_y2r6/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmptuj_y2r6', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
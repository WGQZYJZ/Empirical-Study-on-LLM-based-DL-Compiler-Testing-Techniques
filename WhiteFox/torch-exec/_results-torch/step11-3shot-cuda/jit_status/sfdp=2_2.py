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

    def __init__(self, hidden_dim, dropout_p):
        super().__init__()
        self.scale_factor = np.power(hidden_dim, 0.5)
        self.inv_scale_factor = 1 / np.power(hidden_dim, 0.5)

    def forward(self, query, key, value, dropout_p):
        QK = torch.matmul(query, key.transpose(-2, -1))
        scaled_QK = QK.div(self.inv_scale_factor)
        softmax_QK = scaled_QK.softmax(dim=-1)
        dropout_QK = torch.nn.functional.dropout(softmax_QK, p=dropout_p)
        output = dropout_QK.matmul(value)
        return output


hidden_dim = 1
dropout_p = 1
func = Model(32, 0.1).to('cuda')


x1 = torch.randn(1, 16, 32)

x2 = torch.randn(1, 16, 32)

x3 = torch.randn(1, 16, 32)
query = 1

test_inputs = [x1, x2, x3, query]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpisn0idx3/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpisn0idx3/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpisn0idx3', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def __init__(self, num_queries=5, hidden_dim=16, value_dim=16, inv_scale_factor=512, dropout_p=0.1):
        super(Model, self).__init__()
        self.dropout_p = dropout_p
        self.inv_scale_factor = inv_scale_factor
        self.query = torch.nn.Linear(num_queries, hidden_dim)
        self.key = torch.nn.Linear(num_queries, hidden_dim)
        self.value = torch.nn.Linear(num_queries, value_dim)

    def forward(self, x1):
        qk = self.query(x1).unsqueeze(-2) * self.key(x1).unsqueeze(-2).transpose(-2, -1)
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        return torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)


func = Model(num_queries=5).to('cpu')


x1 = torch.randn(1, 5)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpc5ph_8bo/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpc5ph_8bo/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpc5ph_8bo', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
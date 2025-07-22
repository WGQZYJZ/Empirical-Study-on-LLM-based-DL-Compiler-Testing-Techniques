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

    def __init__(self, num_heads=16, batch_size=64, sequence_length=64, hidden_size=512, p=0.0):
        super().__init__()
        num_heads = hidden_size // num_heads
        hidden_size_per_head = hidden_size // num_heads
        self.key = torch.nn.Parameter(torch.randn(hidden_size, hidden_size))
        self.value = torch.nn.Parameter(torch.randn(hidden_size, hidden_size))
        self.query = torch.nn.Parameter(torch.randn(hidden_size, hidden_size))
        self.inv_scale_factor = (hidden_size_per_head ** (-0.25)) ** 0.5
        self.dropout = torch.nn.Dropout(p)

    def forward(self, x1):
        qk = torch.matmul(x1, self.key.transpose(-2, -1))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        output = self.dropout(softmax_qk).matmul(self.value)
        return output


func = Model().to('cpu')


x1 = torch.randn(1, 16, 512)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp7_t_h051/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp7_t_h051/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp7_t_h051', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def __init__(self, input_size, output_size, query_size, dropout_p=0.5):
        super().__init__()
        self.input_size = input_size
        self.output_size = output_size
        self.query_size = query_size
        self.dropout_p = dropout_p
        self.key = torch.nn.Parameter(torch.Tensor(output_size, input_size))
        self.inv_scale_factor = torch.nn.Parameter(torch.Tensor([input_size ** (-0.5)]))
        self.query = torch.nn.Parameter(torch.Tensor(output_size, query_size))
        self.value = torch.nn.Parameter(torch.Tensor(output_size, input_size))
        self.dropout = torch.nn.Dropout(dropout_p)
        self.softmax = torch.nn.Softmax(dim=-1)
        torch.nn.init.normal_(self.key, 0, input_size ** (-0.5))
        torch.nn.init.constant_(self.inv_scale_factor, 1.0)
        torch.nn.init.normal_(self.query, 0, input_size ** (-0.5))
        torch.nn.init.normal_(self.value, 0, input_size ** (-0.5))

    def forward(self, x1, x2):
        qk = torch.tensordot(x1, self.key, dims=1)
        scaled_qk = qk * self.inv_scale_factor ** (-1)
        softmax_qk = torch.nn.functional.dropout(self.softmax(scaled_qk), p=self.dropout_p)
        output = torch.tensordot(softmax_qk, self.value, dims=1)
        return output


input_size = 1
output_size = 1
query_size = 1

func = Model(input_size, output_size, query_size).to('cpu')


x1 = torch.randn(500, 300)

x2 = torch.randn(300, 500)

test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpq6q5brbw/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpq6q5brbw/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpq6q5brbw', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
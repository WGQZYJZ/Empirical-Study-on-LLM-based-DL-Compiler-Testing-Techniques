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

    def __init__(self, input_channels: int, hidden_size: int, num_heads: int, dropout_p: float):
        super().__init__()
        self.num_heads = num_heads
        self.dropout_p = dropout_p
        self.projection = torch.nn.Linear(input_channels, hidden_size)
        self.activation = torch.nn.ReLU()

    def forward(self, x1, x2):
        v1 = self.projection(x1)
        v2 = v1.transpose(-2, -1)
        v3 = torch.matmul(x2, v2)
        v4 = v3.div(self.num_heads ** (-0.5))
        v5 = torch.nn.functional.softmax(v4, dim=-1)
        v6 = torch.nn.functional.dropout(v5, p=self.dropout_p)
        v7 = torch.matmul(v6, x1)
        return v7


input_channels = 1
hidden_size = 1
num_heads = 1
dropout_p = 1
func = Model(8, 4, 8, 0.1).to('cpu')


x1 = torch.randn(1, 4, 8)

x2 = torch.randn(1, 5, 4)

test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpieq32yym/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpieq32yym/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpieq32yym', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
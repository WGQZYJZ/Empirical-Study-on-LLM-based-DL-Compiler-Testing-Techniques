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

    def __init__(self, dim, dropout_p=0.5):
        super().__init__()
        self.dropout_p = dropout_p
        self.q = torch.nn.Parameter(torch.rand(2, dim, requires_grad=True))
        self.k = torch.nn.Parameter(torch.rand(2, dim, requires_grad=True))
        self.v = torch.nn.Parameter(torch.rand(2, dim, requires_grad=True))

    def forward(self, inputs):
        w = torch.matmul(inputs, self.q.transpose(-2, -1))
        w = w / math.sqrt(self.q.shape[-1])
        w = torch.nn.functional.softmax(w, dim=-1)
        w = torch.nn.functional.dropout(w, p=self.dropout_p)
        z = torch.matmul(w, self.v)
        return z


dim = 1
func = Model(3, 0.9).to('cpu')


inputs = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

test_inputs = [inputs]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp7u2gomau/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp7u2gomau/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp7u2gomau', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
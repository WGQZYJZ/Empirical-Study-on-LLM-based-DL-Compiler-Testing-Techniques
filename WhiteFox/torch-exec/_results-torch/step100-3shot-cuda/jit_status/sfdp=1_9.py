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

    def __init__(self, input_dim, output_dim, num_heads, dropout_p=0.1):
        super().__init__()
        self.output_dim = output_dim
        self.num_heads = num_heads
        self.dropout_p = dropout_p
        self.scale_factor = torch.sqrt(torch.tensor(input_dim, dtype=torch.float))
        self.w_q = torch.nn.Linear(input_dim, output_dim, bias=False)
        self.w_k = torch.nn.Linear(input_dim, output_dim, bias=False)
        self.w_v = torch.nn.Linear(input_dim, output_dim, bias=False)

    def forward(self, x1, x2):
        q = self.w_q(x1)
        k = self.w_k(x2)
        v = self.w_v(x2)
        qk = torch.matmul(q, k.transpose(-2, -1)) / self.scale_factor
        softmax_qk = qk.softmax(dim=-1)
        pooled_softmax_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = pooled_softmax_qk.matmul(v)
        return output


input_dim = 1
output_dim = 1
num_heads = 1
func = Model(256, 512, 8).to('cuda')


x1 = torch.randn(2, 8, 256)

x2 = torch.randn(2, 14, 256)

test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpazdvt98e/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpazdvt98e/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpazdvt98e', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
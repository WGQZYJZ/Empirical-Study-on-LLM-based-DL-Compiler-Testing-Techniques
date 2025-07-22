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

    def __init__(self, dropout=0.1):
        super().__init__()
        self.dropout = float(dropout)

    def forward(self, query, key, value):
        output = torch.softmax(query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)), dim=-1)
        output = torch.dropout(output, self.dropout, training=self.training)
        output = output @ value
        return output


func = Model(dropout=0.1).to('cuda')


query = torch.randn(4, 16, 10)

key = torch.randn(4, 32, 10)

value = torch.randn(4, 32, 20)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
dropout() missing 1 required positional arguments: "train"

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpzgrjxk6l/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpzgrjxk6l/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpzgrjxk6l', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def __init__(self, n_features, n_neurons, p):
        super().__init__()
        self.query = torch.nn.Linear(n_features, n_neurons)
        self.key = torch.nn.Linear(n_features, n_neurons)
        self.value = torch.nn.Linear(n_features, n_neurons)
        self.p = p

    def forward(self, x):
        query = self.query(x)
        key = self.key(x)
        value = self.value(x)
        numerator = query @ key.transpose(-2, -1)
        v1 = numerator / math.sqrt(query.size(-1))
        v1 = v1.softmax(dim=-1)
        v2 = torch.nn.functional.dropout(v1, p=self.p, training=self.training)
        v3 = v2 @ value
        return v3


n_features = 1
n_neurons = 1
p = 1
func = Model(100, 200, 0.2).to('cpu')


x = torch.randn(30, 5, 100)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpx3msek7y/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpx3msek7y/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpx3msek7y', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
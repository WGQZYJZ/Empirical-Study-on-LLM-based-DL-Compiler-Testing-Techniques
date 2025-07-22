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
        self.q = torch.nn.Linear(6, 10)
        self.k = torch.nn.Linear(6, 10)
        self.v = torch.nn.Linear(6, 10)

    def forward(self, query, key, value, dropout_p, scale_factor):
        q = self.q(query)
        k = self.k(key)
        v = self.v(value)
        logits = torch.matmul(q, k.transpose(-2, -1) / scale_factor)
        probs = torch.nn.functional.softmax(logits, dim=-1)
        output = torch.nn.functional.dropout(probs, p=dropout_p)
        output = torch.matmul(output, v)
        return output


func = Model().to('cpu')


query = torch.randn(1, 5, 6)

key = torch.randn(1, 5, 6)

value = torch.randn(1, 5, 6)

scale_factor = torch.tensor([0.0001])
dropout_p = 1

test_inputs = [query, key, value, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
dropout(): argument 'p' (position 2) must be float, not Tensor

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_njqo2y2/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp_njqo2y2/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp_njqo2y2', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.attn_mask = nn.Parameter(torch.randn([1, 1, 1, 64], dtype=torch.float32))
        self.attn_q = torch.nn.Linear(8, 8)
        self.attn_k = torch.nn.Linear(8, 8)
        self.attn_v = torch.nn.Linear(8, 8)

    def forward(self, x1, x2):
        q = self.attn_q(x1)
        k = self.attn_k(x2)
        v = self.attn_v(x2)
        qk = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        qk = qk + self.attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_output = attn_weight @ v
        return attn_output


func = Model().to('cpu')


x1 = torch.randn(1, 1, 8)

x2 = torch.randn(1, 64, 8)

test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpym92tlvw/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpym92tlvw/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpym92tlvw', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
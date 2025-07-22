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
        self.q = torch.nn.Linear(6, 1)
        self.k = torch.nn.Linear(6, 1)
        self.v = torch.nn.Linear(6, 1)

    def forward(self, x, mask):
        v1 = self.q(x)
        v2 = self.k(x)
        v3 = self.v(x)
        print(v1.size())
        print(v2.size())
        print(v3.size())
        v4 = v1 @ v2.transpose(-2, -1) / math.sqrt(6)
        v5 = v4 + mask
        v6 = v5 / v5.sum(-1, keepdim=True)
        v7 = v6 @ v3
        return v7


func = Model().to('cpu')


x = torch.randn(1, 6)
mask = 1

test_inputs = [x, mask]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpisgv022l/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpisgv022l/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpisgv022l', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
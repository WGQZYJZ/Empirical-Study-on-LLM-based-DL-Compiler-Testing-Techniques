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

class m1(torch.nn.Module):

    def __init__(self, m2):
        super().__init__()
        self.m2 = m2

    def forward(self, x1):
        x2 = self.m2(x1)
        x3 = torch.randint(0, 9, (1,))
        x4 = torch.rand_like(x3)
        return x4

class m2(torch.nn.Module):

    def __init__(self, p1):
        super().__init__()
        self.p1 = p1

    def forward(self, x1):
        x2 = x1 ** self.p1
        x3 = torch.randint(0, 9, (1,))
        x4 = torch.nn.functional.dropout(x2)
        return x4


p1 = 1

func = m2(p1).to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpvg65u9al/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpvg65u9al/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpvg65u9al', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
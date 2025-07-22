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

class Model1(torch.nn.Module):

    def __init__(self):
        super(Model1, self).__init__()
        self.fc1 = torch.nn.Linear(2, 10)

    def forward(self, x, y, z):
        x = self.fc1(x)
        y1 = x + y
        z1 = x + z
        return (y1, z1)

class Model2(torch.nn.Module):

    def __init__(self, m, n):
        super(Model2, self).__init__()
        self.model = m
        self.fc1 = torch.nn.Linear(n, 10)

    def forward(self, x):
        y = torch.randn(3, 2)
        z = torch.randn(3, 4)
        return self.model(x, y, z)


m = Model1()
n = 1
func = Model2(m, 10).to('cuda')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
linear(): argument 'input' (position 1) must be Tensor, not int

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp358dl_b9/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp358dl_b9/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp358dl_b9', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
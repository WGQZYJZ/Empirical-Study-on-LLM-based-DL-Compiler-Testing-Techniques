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

    def __init__(self, fallback_random=False):
        super().__init__()
        self.conv = torch.nn.Conv2d(2, 2, 2)
        self.batchnorm = torch.nn.BatchNorm2d(2)

    def forward(self, x):
        x1 = self.batchnorm(self.conv(x))
        x2 = x1 + self.conv(x)
        x3 = torch.rand_like(x2) if not fallback_random else None
        x4 = x3 if x3 is not None else self.conv(x1)
        x5 = torch.nn.functional.dropout(x4)
        return x5

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.relu = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x0):
        x = self.linear1(x0)
        x = self.relu(x)
        x = self.linear2(x)
        return x



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2, 2)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpwnmqusqm/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpwnmqusqm/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpwnmqusqm', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
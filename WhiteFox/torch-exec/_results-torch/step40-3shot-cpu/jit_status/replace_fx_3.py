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

    def __init__(self):
        super().__init__()
        self.layers = torch.nn.Sequential(torch.nn.Linear(64, 128), torch.nn.ReLU(), torch.nn.Linear(128, 1))

    def forward(self, inputs):
        x1 = self.layers(inputs)
        x2 = torch.nn.functional.softmax(x1, dim=0)
        x3 = torch.rand_like(x1, dim=0)
        return x2 + x3

class m2(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, inputs):
        x1 = torch.nn.functional.dropout(inputs, p=0.5)
        x2 = x1.sigmoid()
        x3 = torch.rand_like(x1.sigmoid())
        return x2 - x3


func = m2().to('cpu')


inputs = torch.randn(128, 64)

test_inputs = [inputs]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpls3u86eu/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpls3u86eu/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpls3u86eu', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
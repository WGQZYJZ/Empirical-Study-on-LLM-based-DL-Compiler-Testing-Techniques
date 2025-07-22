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

    def __init__(self, negative_slope=0.01):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(64, 128)
        self.negative_slope = torch.nn.parameter.Parameter(torch.tensor(negative_slope))

    def forward(self, x1):
        v1 = torch.nn.functional.leaky_relu(self.linear(x1), negative_slope=self.negative_slope)
        return v1


func = Model().to('cuda')


x1 = torch.randn(8, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
leaky_relu(): argument 'negative_slope' (position 2) must be Number, not Parameter

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpr3i1sfjx/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpr3i1sfjx/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpr3i1sfjx', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
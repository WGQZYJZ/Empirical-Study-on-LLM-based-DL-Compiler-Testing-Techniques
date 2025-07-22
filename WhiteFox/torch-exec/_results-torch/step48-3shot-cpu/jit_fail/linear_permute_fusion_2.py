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
        self.linear1 = torch.nn.Linear(2, 4)

    def forward(self, x0):
        v0 = x0
        v1 = torch.nn.functional.linear(v0, self.linear1.weight, self.linear1.bias)
        v2 = v1.permute(0, 2, 1)
        v3 = v2.reshape(1, 8, 1)
        self.linear2 = torch.nn.Linear(1, 2)
        v4 = torch.nn.functional.linear(v3, self.linear2.weight, self.linear2.bias)
        v5 = v4.reshape(1, 2, 2)
        return v5



func = Model().to('cpu')


x0 = torch.randn(1, 2, 2)

test_inputs = [x0]

# JIT_FAIL
'''
direct:
shape '[1, 2, 2]' is invalid for input of size 16

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmphaniv3ns/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmphaniv3ns/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmphaniv3ns', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
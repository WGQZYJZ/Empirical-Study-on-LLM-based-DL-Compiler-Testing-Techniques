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
        self.conv = torch.nn.Conv2d(1, 10, 1, stride=1, padding=1)

    def forward(self, x1, other=None):
        v1 = self.conv(x1)
        if other == None:
            other = torch.randn(v1.shape)
        if other == 1:
            v2 = v1 + other
        elif other == 2:
            v3 = v1 + other + 1
        elif other == 3:
            v4 = v1 + other + 2
        elif other == 4:
            v5 = v1 + other + 3
        elif other == 5:
            v6 = v1 + other + 4
        elif other == 6:
            v7 = v1 + other + 5
        elif other == 7:
            v8 = v1 + other + 6
        elif other == 8:
            v9 = v1 + other + 7
        elif other == 9:
            v10 = v1 + other + 8
        else:
            v11 = v1 + other + 9
        return v1



func = Model().to('cpu')


x1 = torch.randn(2, 1, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Boolean value of Tensor with more than one value is ambiguous

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp8esa_02q/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp8esa_02q/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp8esa_02q', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
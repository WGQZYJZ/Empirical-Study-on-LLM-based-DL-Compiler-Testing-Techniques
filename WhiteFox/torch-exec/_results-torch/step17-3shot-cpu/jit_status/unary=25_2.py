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

    def __init__(self, negative_slope):
        super().__init__()
        self.linear = torch.nn.Linear(16, 32)
        self.negative_slope = negative_slope

    def forward(self, x1):
        w1 = self.linear(x1)
        w2 = w1 > 0
        w3 = w1 * self.negative_slope
        w4 = torch.where(w2, w1, w3)
        return w4


negative_slope = 1
func = Model(0.01).to('cpu')


x1 = torch.randn(32, 16)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpqb16_gop/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpqb16_gop/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpqb16_gop', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
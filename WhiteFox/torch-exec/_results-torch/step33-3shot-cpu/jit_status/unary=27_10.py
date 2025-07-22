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

    def __init__(self, min, max):
        super().__init__()
        self.max1 = torch.nn.MaxPool2d(7, stride=5, padding=2)
        self.max2 = torch.nn.MaxPool2d(5, stride=3, padding=2)
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = self.max2
        v2 = self.max1
        v3 = v1(self.max2(x1))
        v4 = v2(self.max2(x1))
        v5 = torch.clamp_min(v3, self.min)
        v6 = torch.clamp_max(v5, self.max)
        return 2 * v6


min = 0.365801
max = 1.5579

func = Model(min, max).to('cpu')


x1 = torch.randn(1, 8, 58, 58)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp38rb_2pw/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp38rb_2pw/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp38rb_2pw', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
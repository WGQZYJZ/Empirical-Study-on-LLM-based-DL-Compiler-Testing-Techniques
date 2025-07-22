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

    def __init__(self, min_value, max_value):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)
        self.avgpool = torch.nn.AvgPool2d(3, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = self.avgpool(t1)
        t3 = torch.clamp_min(t2, self.min_value)
        t4 = torch.clamp_max(t3, self.max_value)
        return t4


min_value = 0.77
max_value = 0.8

func = Model(min_value, max_value).to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmprel_6m8d/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmprel_6m8d/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmprel_6m8d', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv1 = torch.nn.Conv2d(4, 13, 1, stride=1, padding=0)
        self.t1 = torch.nn.Tanh()
        self.conv2 = torch.nn.Conv2d(13, 3072, 11, stride=11, padding=0)
        self.t2 = torch.nn.Tanh()
        self.conv3 = torch.nn.Conv2d(3072, 1000, 1, stride=1, padding=0)
        self.t3 = torch.nn.Tanh()

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.t1(v1)
        v3 = self.conv2(v2)
        v4 = self.t2(v3)
        v5 = self.conv3(v4)
        v6 = self.t3(v5)
        return v6



func = Model().to('cpu')


x = torch.randn(1, 4, 318, 255)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpsz6i41id/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpsz6i41id/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpsz6i41id', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        super(Model, self).__init__()
        self.c1 = torch.nn.Conv2d(in_channels=2, out_channels=3, kernel_size=1, stride=1, padding=0)

    def forward(self, x1, x2, x3, x4):
        x1 = self.c1(x1)
        x2 = self.c1(x2)
        x3 = self.c1(x3)
        x4 = self.c1(x4)
        x5 = x1 + x2
        x6 = x3 + x4
        x7 = x5 + x6
        return x7



func = Model().to('cpu')


x1 = torch.randn(24, 2, 10, 5)

x2 = torch.randn(24, 2, 10, 5)

x3 = torch.randn(24, 2, 10, 5)

x4 = torch.randn(24, 2, 10, 5)

test_inputs = [x1, x2, x3, x4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpwte3mw3f/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpwte3mw3f/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpwte3mw3f', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.module1 = torch.nn.Conv2d(196, 48, kernel_size=(1, 1), stride=(1, 1))
        self.module2 = torch.nn.ReLU()
        self.module3 = torch.nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = self.module1(x1)
        v2 = self.module2(v1)
        v3 = self.module3(v2)
        v4 = torch.clamp_min(v3, self.min)
        v5 = torch.clamp_max(v4, self.max)
        return v5


min = 0.002
max = 0.003

func = Model(min, max).to('cpu')


x1 = torch.randn(1, 196, 87, 73)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpp6j7sm43/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpp6j7sm43/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpp6j7sm43', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
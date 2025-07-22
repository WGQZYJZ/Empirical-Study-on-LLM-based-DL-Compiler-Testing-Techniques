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
        self.block0 = torch.nn.Sequential(torch.nn.ConvTranspose2d(1, 32, 2, padding=1, stride=2), torch.nn.ReLU(inplace=True))
        self.block1 = torch.nn.Sequential(torch.nn.ConvTranspose2d(32, 64, 3, padding=2, stride=1), torch.nn.ReLU(inplace=False))
        self.block2 = torch.nn.Sequential(torch.nn.ConvTranspose2d(64, 64, 3, padding=1, stride=1), torch.nn.ReLU(inplace=True))
        self.block3 = torch.nn.Sequential(torch.nn.ConvTranspose2d(64, 1, 3, padding=1, stride=1), torch.nn.ReLU(inplace=False), torch.nn.Sigmoid())

    def forward(self, x1):
        x2 = x1
        x3 = self.block0(x2)
        x4 = x3
        x5 = self.block1(x4)
        x6 = x5
        x7 = self.block2(x6)
        x8 = x7
        y = self.block3(x8)
        return y



func = Model().to('cpu')


x1 = torch.randn(1, 1, 112, 112)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpid2oe7k6/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpid2oe7k6/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpid2oe7k6', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
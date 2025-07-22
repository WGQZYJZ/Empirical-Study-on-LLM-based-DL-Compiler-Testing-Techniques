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
        self.conv1 = torch.nn.Conv2d(4, 4, 1, bias=False)
        self.bn1 = torch.nn.BatchNorm2d(4)
        self.conv1d = torch.nn.Conv2d(4, 4, 1, bias=False)
        self.bn1d = torch.nn.BatchNorm2d(4)
        self.conv2 = torch.nn.Conv2d(4, 4, 3, padding=1, bias=False)
        self.bn = torch.nn.BatchNorm2d(4)
        self.conv3d = torch.nn.Conv2d(4, 4, 3, padding=1, bias=False)
        self.bn3d = torch.nn.BatchNorm2d(4)

    def forward(self, x):
        x = self.bn1(self.conv1(x))
        x = x + self.bn1d(self.conv1d(x))
        x = self.bn(self.conv2(x))
        x = self.bn3d(self.conv3d(x))
        return x



func = Model().to('cpu')


x = torch.randn(1, 4, 6, 6)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp3aujqh8m/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp3aujqh8m/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp3aujqh8m', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv0 = torch.nn.Conv2d(2, 29, 1, stride=1, padding=0)
        self.relu0 = torch.nn.ReLU()
        self.conv1 = torch.nn.Conv2d(29, 80, 1, stride=1, padding=0)
        self.bn1 = torch.nn.BatchNorm2d(80)
        self.relu1 = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(80, 3, 1, stride=1, padding=0)
        self.relu2 = torch.nn.ReLU()

    def forward(self, x6):
        v1 = self.conv0(x6)
        v2 = self.relu0(v1)
        v3 = self.conv1(v2)
        v4 = self.bn1(v3)
        v5 = self.relu1(v4)
        v6 = self.conv2(v5)
        v7 = self.relu2(v6)
        return v7



func = Model().to('cpu')


x6 = torch.randn(1, 2, 51, 17)

test_inputs = [x6]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpi8hzkcj3/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpi8hzkcj3/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpi8hzkcj3', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
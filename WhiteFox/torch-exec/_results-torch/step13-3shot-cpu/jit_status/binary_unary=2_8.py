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
        self.norm1 = torch.nn.BatchNorm2d(20)
        self.norm2 = torch.nn.BatchNorm2d(60)
        self.conv1 = torch.nn.Conv2d(3, 20, 5, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(20, 60, 5, stride=2, padding=2)

    def forward(self, x1):
        v1 = self.norm1(self.conv1(x1))
        v2 = v1 - 10
        v3 = F.relu(v2)
        v4 = self.norm2(self.conv2(v3))
        v5 = v4 - 11
        v6 = F.hardtanh(v5)
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp3pw3dshd/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp3pw3dshd/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp3pw3dshd', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
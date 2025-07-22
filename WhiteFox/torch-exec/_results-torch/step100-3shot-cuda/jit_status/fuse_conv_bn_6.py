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
        self.block1 = torch.nn.Sequential(torch.nn.Conv2d(3, 3, 3, padding=1), torch.nn.BatchNorm2d(3, affine=True))
        self.block2 = torch.nn.Sequential(torch.nn.Conv2d(3, 3, 3), torch.nn.BatchNorm2d(3, affine=False))
        torch.manual_seed(2)
        self.dropout = torch.nn.Dropout(p=0.4)
        self.relu = torch.nn.ReLU()
        torch.manual_seed(3)
        self.pooling = torch.nn.AvgPool2d(3, ceil_mode=True)

    def forward(self, x1):
        s1 = self.block1(x1)
        s2 = self.block2(s1)
        s2 = self.dropout(s2)
        s2 = self.relu(s2)
        s2 = self.pooling(s2)
        return s2



func = Model().to('cuda')


x1 = torch.randn(1, 3, 4, 4)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpacd752oo/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpacd752oo/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpacd752oo', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
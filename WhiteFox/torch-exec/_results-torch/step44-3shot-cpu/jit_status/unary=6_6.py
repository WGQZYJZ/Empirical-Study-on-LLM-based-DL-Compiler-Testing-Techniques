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
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=1, padding=0)
        self.batchnorm_1 = torch.nn.BatchNorm2d(3)
        self.conv_1 = torch.nn.Conv2d(3, 3, 3, stride=1, padding=1)
        self.batchnorm_2 = torch.nn.BatchNorm2d(3)
        self.conv_2 = torch.nn.Conv2d(3, 3, 3, stride=1, padding=1)
        self.batchnorm_3 = torch.nn.BatchNorm2d(3)
        self.conv_3 = torch.nn.Conv2d(3, 3, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.batchnorm_1(self.conv(x1)) + self.batchnorm_2(self.conv(x1)) + self.batchnorm_3(self.conv(x1))
        v2 = self.conv_1(self.conv(x1)) + self.conv_2(self.conv(x1)) + self.conv_3(self.conv(x1))
        v3 = v1 + v2
        v4 = torch.clamp_min(v3, 0)
        v5 = torch.clamp_max(v4, 6)
        v6 = self.batchnorm_1(v5) + self.batchnorm_2(v5) + self.batchnorm_3(v5)
        v7 = self.conv_1(v5) + self.conv_2(v5) + self.conv_3(v5)
        v8 = v6 + v7
        v9 = v8 / 6
        v10 = self.conv(x1) + v9
        v11 = self.conv(x1) + v9
        return self.conv_1(v10)



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpv0l8re_8/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpv0l8re_8/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpv0l8re_8', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
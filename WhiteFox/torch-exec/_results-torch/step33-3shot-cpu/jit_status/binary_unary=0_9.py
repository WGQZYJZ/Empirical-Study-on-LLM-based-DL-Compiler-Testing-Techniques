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
        self.conv1 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv6 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)
        self.conv7 = torch.nn.Conv2d(16, 16, 3, stride=1, padding=1)

    def forward(self, x):
        v = self.conv1(x)
        v1 = v + x
        v2 = self.conv2(v1)
        v3 = v1 + v2
        v4 = self.conv3(v3)
        v5 = v + v2
        v6 = self.conv4(v5)
        v7 = self.conv5(v1)
        v8 = v7 + v2
        v9 = v4 * v6
        v10 = v9 * v8
        v11 = self.conv6(v10)
        v12 = self.conv7(v3)
        v13 = v11 + v12
        v14 = torch.tanh(v13)
        return v13



func = Model().to('cpu')


x = torch.randn(1, 16, 32, 32)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpvudb5ja_/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpvudb5ja_/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpvudb5ja_', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
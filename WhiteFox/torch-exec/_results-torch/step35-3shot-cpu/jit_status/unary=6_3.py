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
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(3)
        self.relu1 = torch.nn.ReLU(inplace=False)
        self.bn2 = torch.nn.BatchNorm2d(3)
        self.relu2 = torch.nn.ReLU(inplace=False)
        self.bn3 = torch.nn.BatchNorm2d(3)
        self.relu3 = torch.nn.ReLU(inplace=False)
        self.bn4 = torch.nn.BatchNorm2d(3)
        self.relu4 = torch.nn.ReLU(inplace=False)
        self.bn5 = torch.nn.BatchNorm2d(3)
        self.relu5 = torch.nn.ReLU(inplace=False)
        self.bn6 = torch.nn.BatchNorm2d(3)
        self.relu6 = torch.nn.ReLU(inplace=False)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = 3 + v1
        v6 = v2 / 6
        v7 = self.bn1(v6)
        v8 = self.relu1(v7)
        v9 = self.bn2(v8)
        v10 = self.relu2(v9)
        v11 = v10 / 6
        v12 = self.bn3(v11)
        v13 = self.relu3(v12)
        v14 = self.bn4(v13)
        v15 = self.relu4(v14)
        v16 = v15 / 6
        v17 = self.bn5(v16)
        t1 = self.relu5(v17)
        v18 = torch.clamp_min(t1, 0)
        v19 = torch.clamp_max(v18, 6)
        v20 = v16 * v19
        v21 = v20 / 6
        v22 = self.bn6(v21)
        v23 = self.relu6(v22)
        return v23



func = Model().to('cpu')


x1 = torch.randn(2, 3, 64, 64)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpyqcs06f_/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpyqcs06f_/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpyqcs06f_', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
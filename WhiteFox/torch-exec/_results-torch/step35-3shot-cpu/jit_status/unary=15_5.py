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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 3, stride=1, padding=2)
        self.conv3 = torch.nn.Conv2d(8, 8, 3, stride=2, padding=0)
        self.conv4 = torch.nn.Conv2d(8, 8, 3, stride=2, padding=0)
        self.conv5 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0)
        self.conv6 = torch.nn.Conv2d(8, 8, 3, stride=1, padding=1)
        self.conv7 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=0)
        self.conv8 = torch.nn.Conv2d(8, 8, 5, stride=2, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = self.conv2(v2)
        v4 = self.conv3(v3)
        v5 = torch.relu(v4)
        v6 = self.conv4(v5)
        v7 = self.conv5(v6)
        v8 = torch.relu(v7)
        v9 = self.conv6(v8)
        v10 = self.conv7(v9)
        v11 = torch.relu(v10)
        v12 = self.conv8(v11)
        return v12



func = Model().to('cpu')


x1 = torch.randn(1, 3, 288, 72)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmplxc8l7yn/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmplxc8l7yn/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmplxc8l7yn', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
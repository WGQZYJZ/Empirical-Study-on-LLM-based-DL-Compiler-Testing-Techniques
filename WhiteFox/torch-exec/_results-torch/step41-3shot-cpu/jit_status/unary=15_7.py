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
        self.conv1 = torch.nn.Conv2d(3, 8, 5, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 256, 1, stride=1, padding=1)
        self.relu3 = torch.nn.ReLU()

    def forward(self, x1):
        v1 = self.conv1(x1)
        v1 = torch.relu(v1)
        v1 = self.conv2(v1)
        v1 = self.relu3(v1)
        v1 = v1.permute(0, 2, 3, 1)
        v1 = v1.flatten(start_dim=0, end_dim=1)
        v1 = torch.nn.functional.normalize(v1, p=2, dim=1)
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 3, 300, 300)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmppk5zjion/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmppk5zjion/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmppk5zjion', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
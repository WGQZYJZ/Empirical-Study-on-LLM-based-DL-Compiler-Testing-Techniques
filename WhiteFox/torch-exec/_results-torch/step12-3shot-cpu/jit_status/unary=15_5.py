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
        self.conv1 = torch.nn.Conv2d(3, 64, 3, stride=2, padding=0, dilation=1)
        self.conv2 = torch.nn.Conv2d(64, 128, 3, stride=1, padding=1, dilation=1)
        self.bn1 = torch.nn.BatchNorm2d(128)
        self.conv3 = torch.nn.Conv2d(128, 128, 3, stride=1, padding=1, dilation=1)
        self.bn2 = torch.nn.BatchNorm2d(128)
        self.conv4 = torch.nn.Conv2d(128, 64, 1, stride=1, padding=0, dilation=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.bn1(self.conv2(v1))
        v3 = torch.relu(v2)
        v4 = self.bn2(self.conv3(v3))
        v5 = torch.relu(v4)
        v6 = self.conv4(v5)
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 3, 256, 256)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpkng2vstj/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpkng2vstj/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpkng2vstj', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
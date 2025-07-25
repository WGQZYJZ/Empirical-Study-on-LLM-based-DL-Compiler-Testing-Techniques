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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.pad = torch.nn.ReflectionPad2d(2)
        self.conv1 = torch.nn.Conv2d(1, 3, 7, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(3, 5, 3, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(5, 7, 2, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(7, 9, 3, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(9, 11, 7, stride=1, padding=3)

    def forward(self, x):
        v1 = self.pad(x)
        v2 = self.conv1(v1)
        v3 = torch.tanh(v2)
        v4 = self.conv2(v3)
        v5 = torch.tanh(v4)
        v6 = self.conv3(v5)
        v7 = torch.tanh(v6)
        v8 = self.conv4(v7)
        v9 = torch.tanh(v8)
        v10 = self.conv5(v9)
        return v10



func = ModelTanh().to('cpu')


x = torch.randn(3, 1, 13, 17)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpso8iman9/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpso8iman9/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpso8iman9', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
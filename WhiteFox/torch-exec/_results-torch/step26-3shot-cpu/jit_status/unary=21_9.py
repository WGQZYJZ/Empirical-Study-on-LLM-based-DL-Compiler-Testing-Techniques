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
        self.conv2d = torch.nn.Conv2d(3, 32, 7, 3)
        self.conv2d_1 = torch.nn.Conv2d(32, 48, 5, 1)
        self.conv2d_2 = torch.nn.ConvTranspose2d(48, 64, 2, 1)
        self.maxpool2d = torch.nn.MaxPool2d(kernel_size=3, stride=3, padding=1)
        self.avgpool2d = torch.nn.AvgPool2d(kernel_size=3, stride=2, padding=0)
        self.tanh = torch.nn.Tanh()
        self.softmax = torch.nn.Softmax()

    def forward(self, x):
        v1 = self.conv2d(x)
        v2 = self.conv2d_1(v1)
        v3 = self.conv2d_2(v2)
        v4 = self.maxpool2d(v3)
        v5 = self.avgpool2d(v4)
        x1 = self.tanh(v5)
        x2 = self.softmax(x1)
        return x2



func = ModelTanh().to('cpu')


x = torch.randn(64, 3, 112, 112)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp99wc7tay/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp99wc7tay/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp99wc7tay', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
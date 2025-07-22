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

class tanhActivation(torch.nn.Module):

    def forward(self, x1):
        result = torch.tanh(x1)
        y = torch.add(x1, result)
        return result

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_1 = torch.nn.Conv2d(3, 16, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
        self.batchnorm2d = torch.nn.BatchNorm2d(16)
        self.tanh = tanhActivation()
        self.conv_2 = torch.nn.Conv2d(16, 16, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)
        self.batchnorm2d_1 = torch.nn.BatchNorm2d(16)
        self.tanh_1 = tanhActivation()
        self.conv_3 = torch.nn.Conv2d(16, 16, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=False)

    def forward(self, x):
        v1 = self.conv_1(x)
        v2 = self.batchnorm2d(v1)
        v3 = self.tanh(v2)
        v4 = self.conv_2(v3)
        v5 = self.batchnorm2d_1(v4)
        v6 = self.tanh_1(v5)
        v7 = self.conv_3(v6)
        return v7



func = ModelTanh().to('cpu')


x = torch.randn(1, 3, 256, 256)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpavp8xhnk/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpavp8xhnk/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpavp8xhnk', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def __init__(self, min_value=0, max_value=6.4):
        super(Model, self).__init__()
        self.min_value = min_value
        self.max_value = max_value
        self.leaky_relu = torch.nn.LeakyReLU()
        self.dropout = torch.nn.Dropout(0.1)
        self.max_pool2d = torch.nn.MaxPool2d(1, stride=1, padding=0)
        self.conv2d = torch.nn.ConvTranspose2d(3, 16, 1, stride=1, padding=1)

    def forward(self, x):
        v1 = self.dropout(x)
        v4 = self.conv2d(v1)
        v5 = v4.clamp(self.min_value, self.max_value)
        v6 = self.leaky_relu(v5)
        return v6



func = Model().to('cpu')


x3 = torch.randn(1, 3, 224, 224)

test_inputs = [x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp5xwpx0e9/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp5xwpx0e9/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp5xwpx0e9', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
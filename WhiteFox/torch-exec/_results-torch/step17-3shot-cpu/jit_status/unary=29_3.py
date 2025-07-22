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
        self.leaky_rel = torch.nn.LeakyReLU()
        self.dropout = torch.nn.Dropout(0.1)
        self.max_pool2d = torch.nn.MaxPool2d(1, stride=1, padding=0)
        self.relu = torch.nn.ReLU6()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x3):
        v1 = self.dropout(x3)
        v6 = self.conv_transpose(x3)
        v2 = torch.clamp_min(v6, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.leaky_rel(v3)
        v5 = self.relu(v4)
        return v5



func = Model().to('cpu')


x3 = torch.randn(1, 3, 224, 224)

test_inputs = [x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpnrd9ud0n/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpnrd9ud0n/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpnrd9ud0n', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
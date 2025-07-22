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
        self.ConvTranspose_pointwise = torch.nn.ConvTranspose2d(4, 16, (3, 4), stride=(2, 3), padding=(0, 1), dilation=2, output_padding=1)
        self.BatchNorm2d = torch.nn.BatchNorm2d(16)
        self.relu = torch.nn.ReLU()
        self.ReLU_fusion = torch.nn.RReLU(0.1, 0.3)

    def forward(self, x1):
        v1 = self.ConvTranspose_pointwise(x1)
        v2 = self.BatchNorm2d(v1)
        v3 = self.relu(v2)
        v4 = self.ReLU_fusion(v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 4, 64, 64)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmporc8ndai/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmporc8ndai/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmporc8ndai', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
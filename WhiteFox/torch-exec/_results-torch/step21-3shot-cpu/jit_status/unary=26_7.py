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
        self.conv_t = torch.nn.ConvTranspose2d(128, 88, 1, bias=True, stride=1, padding=0)
        self.conv = torch.nn.Conv2d(88, 23, 3, stride=1, padding=0, bias=False)

    def forward(self, x7):
        x8 = self.conv_t(x7)
        x9 = self.conv(x8)
        x10 = x9 < 1
        x11 = x9 > 1
        x12 = x9 / 3
        x13 = torch.where(x10, x9, x12)
        x14 = torch.where(x11, x9, x13)
        return x14



func = Model().to('cpu')


x7 = torch.randn(8, 128, 4, 4)

test_inputs = [x7]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmporxnlhm8/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmporxnlhm8/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmporxnlhm8', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
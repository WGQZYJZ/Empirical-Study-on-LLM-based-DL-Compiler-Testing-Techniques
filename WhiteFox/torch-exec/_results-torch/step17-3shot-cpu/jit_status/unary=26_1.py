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

    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv = torch.nn.Conv2d(32, 1, (1, 3), 1, padding=(0, 1), groups=1, bias=False)
        self.conv_t = torch.nn.ConvTranspose2d(1, 32, 4, stride=3, padding=1, groups=1, dilation=1, output_padding=0, bias=False)

    def forward(self, img):
        x = self.conv(img)
        x = self.conv_t(x)
        y = x > 0
        z = torch.where(y, x, x * negative_slope)
        return z



func = Model().to('cpu')


img = torch.randn(1, 32, 64, 64)

test_inputs = [img]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpwow1va8k/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpwow1va8k/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpwow1va8k', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
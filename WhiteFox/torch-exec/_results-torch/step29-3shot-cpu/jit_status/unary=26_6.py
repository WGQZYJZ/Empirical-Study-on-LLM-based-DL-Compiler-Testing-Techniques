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
        self.conv_t1 = torch.nn.ConvTranspose2d(95, 60, 1, stride=1, padding=0)
        self.conv_t2 = torch.nn.ConvTranspose2d(60, 11, 3, stride=2, padding=0)

    def forward(self, x):
        t1 = self.conv_t1(x)
        t2 = torch.clamp(t1, max=3)
        t3 = t1 > 3
        t4 = t1 * 0.5
        t5 = torch.where(t3, t1, t4)
        t6 = t5 == t2
        t7 = t5 > 0
        t8 = t5 * 0.2
        t9 = torch.where(t7, t5, t8)
        x = self.conv_t2(t9)
        return x



func = Model().to('cpu')


x = torch.randn(1, 95, 224, 224)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpz2s5b43x/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpz2s5b43x/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpz2s5b43x', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
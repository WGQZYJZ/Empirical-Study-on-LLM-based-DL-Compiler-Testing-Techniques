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
        self.conv_t1 = torch.nn.ConvTranspose2d(337, 99, 3, stride=2, padding=3, output_padding=1, bias=False)
        self.conv_t2 = torch.nn.ConvTranspose2d(99, 3, 3, stride=1, padding=0, bias=True)

    def forward(self, x5):
        r1 = self.conv_t1(x5)
        r2 = r1 > 0.0
        r3 = r1 * -0.08
        r4 = torch.where(r2, r1, r3)
        r5 = self.conv_t2(r4)
        r6 = r5 > 0.0
        r7 = r5 * -0.41
        r8 = torch.where(r6, r5, r7)
        return r8



func = Model().to('cpu')


x5 = torch.randn(43, 337, 19, 28)

test_inputs = [x5]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpko6xaa8j/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpko6xaa8j/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpko6xaa8j', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
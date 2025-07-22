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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other_conv = torch.nn.Conv2d(8, 8, 9)

    def forward(self, x1):
        v1 = self.conv(x1)
        v1.sub_(3)
        v2 = v1.clamp(min=0, max=6)
        v3 = v2 / 6
        v4 = self.other_conv(v3)
        v5 = v4.add_(6)
        v6 = v5.clamp(min=0, max=6, out=None)
        v7 = v6.clamp(max=2, out=v6)
        return v7



func = Model().to('cpu')


x1 = torch.randn(2, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
clamp() received an invalid combination of arguments - got (out=NoneType, max=int, min=int, ), but expected one of:
 * (Tensor min = None, Tensor max = None)
 * (Number min = None, Number max = None)


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp5fv58iqh/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp5fv58iqh/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp5fv58iqh', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
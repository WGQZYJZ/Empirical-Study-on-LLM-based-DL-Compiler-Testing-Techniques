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

    def forward(self, x1):
        v1 = torch.conv2d(input=x1, weight=torch.nn.Parameter(torch.ones(5, 3, 3, 3)), bias=None, stride=(2, 2), padding=(0, 0), dilation=1, groups=1) * 0.5
        v2 = torch.conv2d(input=x1, weight=torch.nn.Parameter(torch.ones(5, 3, 3, 3)), bias=None, stride=(2, 2), padding=(0, 0), dilation=1, groups=1) * 0.7071067811865476
        v3 = torch.erf(input=v2)
        v4 = v3 + 1
        v5 = v1 * v4
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 3, 28, 28)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpmr019saj/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpmr019saj/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpmr019saj', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
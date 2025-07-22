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

    def forward(self, x1, x2, x3, x4, x5, x6, x7):
        v3 = torch.mm(x3, x7)
        v6 = torch.mm(x6, x5)
        v4 = torch.mm(x4, v6)
        v1 = torch.mm(v3, v6)
        v2 = torch.mm(v4, x6)
        return v1 + v2



func = Model().to('cpu')


x1 = torch.randn(2, 2)

x2 = torch.randn(2, 2)

x3 = torch.randn(2, 2)

x4 = torch.randn(2, 2)

x5 = torch.randn(2, 2)

x6 = torch.randn(2, 2)

x7 = torch.randn(2, 2)

test_inputs = [x1, x2, x3, x4, x5, x6, x7]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpvzi7_823/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpvzi7_823/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpvzi7_823', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
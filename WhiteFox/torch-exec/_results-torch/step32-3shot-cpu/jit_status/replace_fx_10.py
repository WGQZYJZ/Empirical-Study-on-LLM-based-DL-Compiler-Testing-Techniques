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

class model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        y1 = torch.randn(1)
        y2 = torch.randn(1)
        m = torch.nn.Dropout(0.3)
        y3 = m(y1)
        y4 = y3 * 2
        y5 = y2 + y4
        x1 = torch.nn.functional.dropout(x, p=0.1)
        z1 = x1 * 5
        z2 = z1 + y5
        return z2



func = model().to('cpu')


x1 = torch.randn(1, requires_grad=True)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpq6mdngcf/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpq6mdngcf/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpq6mdngcf', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
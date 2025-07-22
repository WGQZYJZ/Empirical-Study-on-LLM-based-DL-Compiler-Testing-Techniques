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

    def forward(self, a, b, c, d, e):
        g1 = torch.mm(a, b)
        g2 = torch.mm(e, e)
        g = g1 + g2
        g3 = torch.mm(d, e)
        g4 = torch.mm(d, e)
        return g + g3 + g4



func = Model().to('cuda')


a = torch.randn(2, 2, requires_grad=True)

b = torch.randn(2, 2, requires_grad=True)

c = torch.randn(4, 2, requires_grad=True)

d = torch.randn(4, 2, requires_grad=True)
e = 1

test_inputs = [a, b, c, d, e]

# JIT_FAIL
'''
direct:
mm(): argument 'input' (position 1) must be Tensor, not int

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp3xsf0ge7/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp3xsf0ge7/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp3xsf0ge7', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
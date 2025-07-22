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

    def forward(self, x1, x2, x3):
        v = []
        v2 = []
        v3 = []
        v.append(torch.mm(x1, x1))
        v.append(x2 + torch.mm(x2, x3))
        if torch.sum(x1) != 0:
            v2.append(x1)
        for j in range(10):
            if torch.sum(x2) != 0:
                v3.append(x2)
        return torch.cat(v, 1) + torch.cat(v2, 1) + v[0].clamp(max=20)



func = Model().to('cpu')


x1 = torch.randn(5, 5)

x2 = torch.randn(5, 5)

x3 = torch.randn(5, 5)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (5) at non-singleton dimension 1

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpv_q2_zuq/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpv_q2_zuq/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpv_q2_zuq', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def forward(self, i1, i2, i3, i4):
        t1 = torch.mm(i1, i2)
        t2 = torch.mm(i3, i4)
        return torch.matmul(t1, t2)



func = Model().to('cuda')


i1 = torch.randn(3, 3)

i2 = torch.randn(3, 3)

i3 = torch.randn(3, 3)

i4 = torch.randn(3, 3)

test_inputs = [i1, i2, i3, i4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp5swcvh68/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp5swcvh68/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp5swcvh68', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        v1 = torch.cat([x1] * 1, 1)
        v2 = torch.cat([x1] * 2, 1)
        v3 = torch.cat([x1] * 3, 1)
        v4 = torch.cat([x1] * 4, 1)
        v5 = torch.cat([v1] * 2, 1)
        v6 = torch.cat([v1, v2, v3], 1)
        v7 = torch.cat([v5, v2, x1, v5], 1)
        v8 = torch.cat([v7] * 5, 1)
        return torch.cat([v6, v1, v2, v3, v4, v5, v6, v7, v8], 1)



func = Model().to('cuda')


x1 = torch.randn(10, 10, 1)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpt_cwxd6l/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpt_cwxd6l/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpt_cwxd6l', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
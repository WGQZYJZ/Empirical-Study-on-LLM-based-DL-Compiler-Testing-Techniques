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

    def forward(self, x):
        y = x.view(x.shape[0], -1)
        if True:
            k = y.unsqueeze(-1).expand(-1, -1, 3)
        else:
            k = y.unsqueeze(-1).expand(-1, -1, 2)
        for i in range(0, 2):
            if i == 1:
                y = torch.cat((y, y), dim=1)
        k = y.view(x.shape[0], -1).tanh()
        for i in range(0, 2):
            k.sin()
            if i == 1:
                k = k.view(x.shape[0], -1).sin()
        y = k.view(y.shape[0], -1).tanh()
        y = y.sum(dim=1, keepdim=True)
        return y



func = Model().to('cpu')


x = torch.randn(2, 3, 4)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp1rw9iov8/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp1rw9iov8/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp1rw9iov8', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.convTranspose1 = torch.nn.ConvTranspose3d(3, 3, kernel_size=(3, 5, 1), stride=(1, 3, 2), padding=(2, 1, 0))

    def forward(self, x1):
        v1 = self.convTranspose1(x1)
        v2 = torch.tanh(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 3, 15, 32, 100)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmptwnru0dd/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmptwnru0dd/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmptwnru0dd', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def __init__(self, a1, b1):
        super().__init__()
        self.a1 = torch.tensor([a1], dtype=torch.float)
        self.b1 = torch.tensor([b1], dtype=torch.float)

    def forward(self, x1):
        x2 = torch.einsum('ij,j->i', x1, F.dropout(self.a1))
        x3 = F.dropout(F.sigmoid(x2))
        x4 = torch.einsum('ij,j->i', x1, F.dropout(self.b1))
        x5 = F.dropout(F.sigmoid(x4))
        x6 = x3 + x5
        x7 = torch.cat((x3, x4), dim=0)
        return x5


a1 = 1
b1 = 2

func = model(a1, b1).to('cpu')


x1 = torch.randn(2, 2)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp31b2cz03/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp31b2cz03/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp31b2cz03', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def forward(self, A, B, C, D, E, F):
        t1 = torch.mm(A, torch.mm(B, torch.mm(C, torch.mm(D, E))))
        t2 = torch.mm(F, torch.mm(E, torch.mm(D, torch.mm(C, B))))
        t2 = t2 + torch.mm(D, torch.mm(C, torch.mm(B, torch.mm(A, F))))
        return t1 + t2



func = Model().to('cpu')


A = torch.randn(4, 4)

B = torch.randn(4, 4)

C = torch.randn(4, 4)

D = torch.randn(4, 4)

E = torch.randn(4, 4)

F = torch.randn(4, 4)

test_inputs = [A, B, C, D, E, F]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpwg_nn9da/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpwg_nn9da/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpwg_nn9da', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
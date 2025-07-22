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

    def __init__(self, p1, p2, p3):
        super(Model, self).__init__()
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def forward(self, x1):
        tmp = torch.nn.functional.dropout(x1, self.p1, True)
        x3 = x1 + tmp
        x2 = torch.randn_like(x1, self.p3)
        x4 = x2 * tmp
        return x1 + x2


p1 = 0.2
p2 = True
p3 = 0

func = Model(p1, p2, p3).to('cpu')


x1 = torch.randn(2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
randn_like() takes 1 positional argument but 2 were given

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpzcmozzxf/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpzcmozzxf/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpzcmozzxf', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

class Mo(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, t0):
        v0 = torch.matmul(t0, t0.transpose(-2, -1))
        v1 = v0.mul(-10000.0)
        v2 = torch.nn.functional.softmax(v1)
        v3 = torch.nn.functional.dropout(v2, 0.0)
        v4 = torch.matmul(v3, t0)
        return v4


func = Mo().to('cpu')


t0 = torch.randn(8, 8, 20)

test_inputs = [t0]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp1xedzfv4/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp1xedzfv4/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp1xedzfv4', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
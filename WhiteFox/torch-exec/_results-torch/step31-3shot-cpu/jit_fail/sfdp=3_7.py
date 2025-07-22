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
        self.softmax = torch.nn.Softmax(dim=-1)

    def forward(self, q1, k1):
        s1 = torch.matmul(q1, k1.transpose(-2, -1))
        s2 = s1 * 0.5
        s3 = s2.transpose(-2, -1)
        s4 = self.softmax(s3)
        s5 = torch.nn.functional.dropout(s4, p=0.5)
        v1 = torch.matmul(s5, v1)
        return v1


func = Model().to('cpu')


q1 = torch.randn(8, 256, 64, 64)

k1 = torch.randn(8, 256, 64, 64)

test_inputs = [q1, k1]

# JIT_FAIL
'''
direct:
local variable 'v1' referenced before assignment

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpcfhrkg4c/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpcfhrkg4c/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpcfhrkg4c', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
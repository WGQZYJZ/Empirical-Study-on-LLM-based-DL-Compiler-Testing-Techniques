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

class Model(nn.Module):

    def forward(self, input_0, input_1, input_2, input_3, input_4, input_5, input_6):
        t0 = torch.matmul(input_0, input_1)
        t1 = torch.matmul(input_2, input_3)
        t2 = torch.matmul(input_4, input_5)
        t3 = torch.matmul(t0, t1)
        t4 = torch.matmul(t2, t3)
        t5 = t4 + input_6
        return t5



func = Model().to('cpu')


input_0 = torch.randn(20, 20, requires_grad=True)

input_1 = torch.randn(20, 20, requires_grad=True)

input_2 = torch.randn(20, 20, requires_grad=True)

input_3 = torch.randn(20, 20, requires_grad=True)

input_4 = torch.randn(20, 20, requires_grad=True)

input_5 = torch.randn(20, 20, requires_grad=True)

input_6 = torch.randn(20, 20, requires_grad=True)

test_inputs = [input_0, input_1, input_2, input_3, input_4, input_5, input_6]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpzq57kwr5/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpzq57kwr5/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpzq57kwr5', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
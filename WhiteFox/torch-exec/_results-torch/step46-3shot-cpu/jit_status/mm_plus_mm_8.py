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

    def forward(self, input1, input2, input3, input4):
        batch_size = input1.shape[0]
        t1 = torch.mm(input1, input2)
        t2 = torch.zeros([batch_size, batch_size], dtype=torch.float)
        for x in range(batch_size):
            for y in range(batch_size):
                t2[x][y] = x + y
        t2 = torch.mm(t2, input3)
        t3 = torch.mm(input4, t2)
        return t1 - t3



func = Model().to('cpu')


N = 10
N = 10
input1 = torch.randn(N, N)

N = 10
N = 10
input2 = torch.randn(N, N)

N = 10
N = 10
input3 = torch.randn(N, N)

N = 10
N = 10
input4 = torch.randn(N, N)

test_inputs = [input1, input2, input3, input4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpebkyrxtt/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpebkyrxtt/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpebkyrxtt', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
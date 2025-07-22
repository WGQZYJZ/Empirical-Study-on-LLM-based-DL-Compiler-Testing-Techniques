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

class Model1(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, input1, input2, input3, input4):
        t1 = torch.matmul(input1, input2)
        t2 = torch.matmul(input3, input4)
        t3 = t1 + t2
        return t3

class Model2(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, input1, input2, input3, input4):
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input3, input4)
        t3 = t1 + t2
        return t3


func = Model2().to('cuda')


input1 = torch.randn(3, 3)

input2 = torch.randn(3, 3)

input3 = torch.randn(3, 3)

input4 = torch.randn(3, 3)

test_inputs = [input1, input2, input3, input4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpg2q6pt3i/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpg2q6pt3i/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpg2q6pt3i', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
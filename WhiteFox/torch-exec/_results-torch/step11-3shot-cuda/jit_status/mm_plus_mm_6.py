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

    def forward(self, input1, input2, input3, input4, input5, input6, input7, input8):
        t1 = torch.mm(input1, input7)
        t2 = torch.mm(input2, input8)
        t3 = t1 + t2
        t4 = torch.mm(input3, input2)
        t5 = torch.mm(input4, input3)
        t6 = torch.mm(input5, input4)
        t7 = torch.mm(input6, input1)
        t8 = t4 + t5 + t6 + t7
        t9 = t3 + t8
        return t9



func = Model().to('cuda')


input1 = torch.randn(5, 5)

input2 = torch.randn(5, 5)

input3 = torch.randn(5, 5)

input4 = torch.randn(5, 5)

input5 = torch.randn(5, 5)

input6 = torch.randn(5, 5)

input7 = torch.randn(5, 5)

input8 = torch.randn(5, 5)

test_inputs = [input1, input2, input3, input4, input5, input6, input7, input8]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpqh1tps2e/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpqh1tps2e/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpqh1tps2e', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
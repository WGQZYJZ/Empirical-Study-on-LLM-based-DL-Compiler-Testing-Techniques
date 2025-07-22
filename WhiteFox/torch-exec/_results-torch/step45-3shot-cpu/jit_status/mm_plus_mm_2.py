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
        t1 = torch.mm(input4, torch.mm(input3, input2))
        t2 = t1 + torch.mm(input2, torch.mm(input3, input1))
        t3 = torch.mm(input6, torch.mm(input5, input4))
        t4 = t2 + t3
        t5 = torch.mm(input7, torch.mm(input6, input5))
        t6 = torch.mm(input8, torch.mm(input7, input3))
        return t5 + torch.mm(input1, t6) + t4



func = Model().to('cpu')


input1 = torch.randn(4, 4)

input2 = torch.randn(4, 4)

input3 = torch.randn(4, 4)

input4 = torch.randn(4, 4)

input5 = torch.randn(4, 4)

input6 = torch.randn(4, 4)

input7 = torch.randn(4, 4)

input8 = torch.randn(4, 4)

test_inputs = [input1, input2, input3, input4, input5, input6, input7, input8]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpx3pid5bo/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpx3pid5bo/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpx3pid5bo', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
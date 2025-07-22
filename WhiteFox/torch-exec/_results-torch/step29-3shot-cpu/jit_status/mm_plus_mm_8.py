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

    def forward(self, input1, input2, input3):
        t1 = nn.Tanh()(input1)
        t2 = input1 + input3
        t3 = nn.PReLU()(-t1)
        t4 = nn.Sigmoid()(input1)
        t5 = nn.Tanh()(input2)
        t6 = nn.Tanh()(input3)
        t7 = input3 + input2
        t8 = nn.ReLU()(input2)
        t9 = nn.ReLU()(t3)
        return t5 + t6 + t7 + t8 + t9



func = Model().to('cpu')


input1 = torch.randn(8, 8)

input2 = torch.randn(8, 8)

input3 = torch.randn(8, 8)

test_inputs = [input1, input2, input3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpubwr513c/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpubwr513c/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpubwr513c', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
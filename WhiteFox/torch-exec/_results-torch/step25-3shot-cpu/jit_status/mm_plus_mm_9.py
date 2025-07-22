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
        self.w1 = torch.randn(2, 2)

    def forward(self, input1, input2, input3, input4):
        v1 = torch.mm(input1, self.w1)
        v2 = torch.mm(input2, self.w1)
        v3 = torch.mm(input3, self.w1)
        v4 = torch.mm(input4, self.w1)
        t1 = torch.mm(v2, v1)
        t2 = torch.mm(v1, v3)
        t3 = torch.mm(v4, v3)
        return t1 + t2 + t3



func = Model().to('cpu')


input1 = torch.randn(2, 2)

input2 = torch.randn(2, 2)

input3 = torch.randn(2, 2)

input4 = torch.randn(2, 2)

test_inputs = [input1, input2, input3, input4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp6ke9jkue/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp6ke9jkue/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp6ke9jkue', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
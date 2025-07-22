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

    def forward(self, input1, input2, input3, input4):
        v1 = input1.view(-1, input1.shape[0])
        v2 = input2.view(-1, input2.shape[0])
        v3 = input3.view(-1, input3.shape[0])
        v4 = input4.view(input4.shape[0], -1)
        v5 = torch.matmul(v1, v2)
        v6 = torch.matmul(v3, v4)
        return v5 + v6



func = Model().to('cpu')


x1 = torch.randn(100, 100)

x2 = torch.randn(100, 100)

x3 = torch.randn(100, 100)

x4 = torch.randn(100, 100)

test_inputs = [x1, x2, x3, x4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpehx49hll/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpehx49hll/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpehx49hll', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
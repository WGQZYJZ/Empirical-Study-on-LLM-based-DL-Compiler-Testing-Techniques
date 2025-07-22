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
        v1 = torch.mm(input1, input2)
        v2 = torch.mm(input3, input4)
        v2 = torch.mm(input1, input2)
        v2 = torch.mm(input1, input2)
        v2 = torch.mm(input1, input2)
        v2 = torch.mm(input1, input2)
        v2 = torch.mm(input1, input2)
        return v1 + v2



func = Model().to('cpu')


input1 = torch.randn(16, 16)

input2 = torch.randn(16, 16)

input3 = torch.randn(16, 16)

input4 = torch.randn(16, 16)

test_inputs = [input1, input2, input3, input4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_sakr5tx/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp_sakr5tx/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp_sakr5tx', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
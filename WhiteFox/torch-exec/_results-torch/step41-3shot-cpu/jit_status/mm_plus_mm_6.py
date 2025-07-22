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

    def forward(self, input1, input2):
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input1, input2)
        t3 = torch.mm(input1, input2) + t1
        t4 = torch.mm(input1, input2) + t2
        t5 = torch.mm(input1, input2) + t1
        t6 = torch.mm(input1, input2) + t1 + t3
        t7 = torch.mm(input1, input2) - torch.mm(input1, input2) - torch.mm(input1, input2) + torch.mm(input1, input2)
        t8 = torch.mm(input1, input2) - torch.mm(input1, input2) - torch.mm(input1, input2) + torch.mm(input1, input2)
        t9 = torch.mm(input1, input2) - t7 - t6
        return torch.mm(input1, input2) - torch.mm(input1, input2) - torch.mm(input1, input2) + torch.mm(input1, input2) - torch.mm(input1, input2) + torch.mm(input1, input2)



func = Model().to('cpu')


input1 = torch.randn(3, 3)

input2 = torch.randn(3, 3)

test_inputs = [input1, input2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp3ft4g8ld/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp3ft4g8ld/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp3ft4g8ld', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
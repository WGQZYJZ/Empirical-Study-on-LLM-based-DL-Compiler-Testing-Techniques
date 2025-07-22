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

    def forward(self, tensorList, tensor2):
        t1 = torch.matmul(tensorList[1], tensorList[2])
        t2 = torch.matmul(tensorList[3], tensorList[4])
        t3 = torch.matmul(tensorList[5], tensorList[7])
        t4 = torch.matmul(tensorList[6], tensor2)
        t5 = t1 + t2
        t6 = t3 + t4
        t7 = t5 + t6
        return t7



func = Model().to('cpu')


tensor2 = torch.randn(20, 20)
tensorList = 1

test_inputs = [tensor2, tensorList]

# JIT_FAIL
'''
direct:
matmul(): argument 'other' (position 2) must be Tensor, not int

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpedmxvf81/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpedmxvf81/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpedmxvf81', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
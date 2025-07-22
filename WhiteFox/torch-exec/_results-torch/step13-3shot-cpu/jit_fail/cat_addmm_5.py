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
        self.weights = torch.nn.Parameter(torch.randn(3, 3))

    def forward(self, x2):
        v1 = torch.cat([x2], dim=1)
        v2 = torch.addmm(input, self.weights, v1)
        return v2


func = Model().to('cpu')


x2 = torch.randn(1, 512, 3, 3)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
addmm(): argument 'input' (position 1) must be Tensor, not builtin_function_or_method

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmplw_is22c/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmplw_is22c/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmplw_is22c', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
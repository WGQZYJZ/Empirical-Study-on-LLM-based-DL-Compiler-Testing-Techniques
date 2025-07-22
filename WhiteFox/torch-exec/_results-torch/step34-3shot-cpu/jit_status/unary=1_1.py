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
        self.Linear_1 = torch.nn.Linear(300, 500)

    def forward(self, x2):
        v233 = torch.nn.functional.linear(x2, self.Linear_1.weight, self.Linear_1.bias)
        v236 = v233 * 0.5
        v239 = torch.mul(v233, v233).mul(v233)
        v242 = v239 * 0.044715
        v248 = v239 * 0.7978845608028654
        v249 = torch.tanh(v248)
        v250 = v249 + 1
        v251 = v236 * v250
        return v251


func = Model().to('cpu')


x2 = torch.randn(1, 300)

test_inputs = [x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpwxu2u8tz/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpwxu2u8tz/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpwxu2u8tz', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
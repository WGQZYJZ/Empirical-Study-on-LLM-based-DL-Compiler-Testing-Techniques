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

    def __init__(self, negative_slope):
        super().__init__()
        self.fc = torch.nn.Linear(8, 8)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = v1[v1 > 0]
        v3 = v1[v2 < 0] * -self.negative_slope
        v4 = torch.where(v1 > 0, v1, v3)
        return v4


negative_slope = 1
func = Model(0.01).to('cpu')


x1 = torch.randn(1, 8)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The shape of the mask [5] at index 0 does not match the shape of the indexed tensor [1, 8] at index 0

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpo4lgjt5k/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpo4lgjt5k/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpo4lgjt5k', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
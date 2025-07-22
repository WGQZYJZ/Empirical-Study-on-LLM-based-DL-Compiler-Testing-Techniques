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

    def __init__(self, min_value, max_value, kernel_size=2):
        super().__init__()
        self.conv = torch.nn.Conv1d(32, 32, 2, stride=2, padding=0, dilation=0)
        self.min_value = min_value
        self.max_value = max_value
        self.kernel_size = 2

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3


min_value = 0.1
max_value = 0.1

func = Model(min_value, max_value).to('cpu')


x1 = torch.randn(1, 32, 100)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
dilation should be greater than zero, but got [1, 0]

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp5zkpjfy2/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp5zkpjfy2/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp5zkpjfy2', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
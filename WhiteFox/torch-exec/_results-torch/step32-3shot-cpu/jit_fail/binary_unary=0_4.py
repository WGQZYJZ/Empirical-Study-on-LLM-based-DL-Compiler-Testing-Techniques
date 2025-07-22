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
        self.conv = torch.nn.Conv2d(16, 16, 11, stride=1, padding=5)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.nn.functional.batch_norm(v1, x.shape[1], eps=0.0001)
        v3 = self.relu(v2)
        v4 = self.conv(v3)
        v5 = torch.squeeze(v4)
        v6 = v5.reshape(1, 8 * 8 * 16)
        v7 = torch.nn.functional.linear(v6, v6)
        v8 = torch.squeeze(v7)
        v9 = self.relu(v8)
        return v9



func = Model().to('cpu')


x = torch.randn(1, 16, 64, 64)

test_inputs = [x]

# JIT_FAIL
'''
direct:
batch_norm() missing 1 required positional argument: 'running_var'

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp0f0stna3/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp0f0stna3/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp0f0stna3', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
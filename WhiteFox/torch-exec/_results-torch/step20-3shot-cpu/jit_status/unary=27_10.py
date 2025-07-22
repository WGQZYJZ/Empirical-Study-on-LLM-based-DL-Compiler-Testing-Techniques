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

    def __init__(self, min_value=0.1, max_value=0.125, alpha=0.2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 1)
        self.min_value = min_value
        self.max_value = max_value
        self.alpha = alpha
        self.activation = torch.nn.Sequential(torch.nn.Conv2d(3, 3, 3, padding=1), torch.nn.ReLU())

    def forward(self, x1):
        v1 = self.conv(x1)
        v1b = v1
        v2 = self.activation(v1)
        v3 = torch.clamp_max(v1b + self.alpha * v2, self.max_value)
        v4 = torch.clamp_min(v3, self.max_value)
        v5 = torch.clamp_max(v4, self.max_value)
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 3, 16, 16)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpb3wf5_sq/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpb3wf5_sq/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpb3wf5_sq', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
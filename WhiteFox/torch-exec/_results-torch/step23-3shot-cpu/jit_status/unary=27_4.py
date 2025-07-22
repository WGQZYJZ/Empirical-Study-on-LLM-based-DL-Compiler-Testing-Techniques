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

    def __init__(self, min_value=0.3, max_value=0.2, p=0.01):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=0.01)
        self.conv = torch.nn.Conv2d(8, 8, 9, stride=1, padding=9)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv(self.dropout(x1))
        v2 = torch.clamp(v1, min=self.min_value, max=self.max_value)
        v3 = torch.abs(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(2, 8, 64, 64)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpr8935eqa/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpr8935eqa/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpr8935eqa', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
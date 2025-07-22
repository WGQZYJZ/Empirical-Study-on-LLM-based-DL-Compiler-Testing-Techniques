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

    def __init__(self, min_value=0.1, max_value=0.6):
        super().__init__()
        self.conv_transpose2d_2 = torch.nn.ConvTranspose2d(16, 16, 3, stride=1, padding=1)
        self.conv_transpose2d_3 = torch.nn.ConvTranspose2d(16, 32, 5, stride=2, padding=2)
        self.conv_transpose2d_4 = torch.nn.ConvTranspose2d(32, 32, 4, stride=2, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x3):
        v5 = self.conv_transpose2d_2(x3)
        v8 = self.conv_transpose2d_3(v5)
        v11 = self.conv_transpose2d_4(v8)
        v13 = v11 + 4.7809789086016155
        v15 = torch.clamp_min(v13, self.min_value)
        v17 = torch.clamp_max(v15, self.max_value)
        return v17



func = Model().to('cpu')


x3 = torch.randn(1, 16, 224, 224)

test_inputs = [x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpljcbnlj8/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpljcbnlj8/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpljcbnlj8', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
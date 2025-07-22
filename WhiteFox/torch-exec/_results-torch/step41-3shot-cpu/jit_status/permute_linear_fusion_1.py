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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v3 = v2.permute(0, 2, 1)
        x2 = torch.sum(x1, dim=1, keepdim=True) * v3 ** 2
        v4 = torch.max(x1, dim=-1, keepdim=True)[0]
        v5 = v4 ** 2
        x3 = x2 ** 2 + v5
        v6 = x2 ** 5 + torch.max(x2, dim=-1, keepdim=True)[0]
        x2 = v2 * x2
        x4 = torch.sqrt(x2 * v6)
        v7 = v5 * torch.sqrt(x4 * v6) ** 2
        v8 = torch.nn.functional.softmax(v7, dim=-1)
        v8 = v8.permute(0, 2, 1)
        v9 = torch.max(x1, dim=-1, keepdim=True)[0]
        x5 = torch.sum(v8) * torch.sum(v9)
        return x5 + v7.permute(0, 2, 1)



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpu_fkri5d/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpu_fkri5d/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpu_fkri5d', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
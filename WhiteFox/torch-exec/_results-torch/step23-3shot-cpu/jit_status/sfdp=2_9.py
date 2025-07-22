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
        self.embed = torch.nn.Linear(16, 32, bias=False)
        self.scale = torch.nn.Parameter(torch.tensor([2000.0]))

    def forward(self, x1):
        v1 = self.embed(x1)
        v2 = v1.transpose(-2, -1)
        v3 = torch.matmul(v1, v2)
        v4 = self.scale.expand_as(v3)
        v5 = v3.div(v4)
        v6 = torch.nn.functional.softmax(v5, -1)
        v7 = torch.nn.functional.dropout(v6, p=0.2, training=True)
        v8 = torch.matmul(v7, v1)
        return v8


func = Model().to('cpu')


x1 = torch.randn(2, 16)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpfqr6sdla/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpfqr6sdla/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpfqr6sdla', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
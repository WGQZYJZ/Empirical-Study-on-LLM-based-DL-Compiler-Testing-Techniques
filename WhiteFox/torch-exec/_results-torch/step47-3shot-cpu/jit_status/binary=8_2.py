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
        self.fc1 = torch.nn.Linear(192, 1)
        self.gelu = torch.nn.GELU()
        self.drop = torch.nn.Dropout(0.6539580252647174)
        self.fc2 = torch.nn.Linear(1, 1)
        self.gelu1 = torch.nn.GELU()
        self.drop1 = torch.nn.Dropout(0.6883371296619819)
        self.fc3 = torch.nn.Linear(1, 1)

    def forward(self, x):
        v1 = self.fc1(x)
        v2 = self.gelu(v1)
        v3 = self.drop(v2)
        v4 = self.fc2(v3)
        v5 = self.gelu1(v4)
        v6 = self.drop1(v5)
        v7 = self.fc3(v6)
        return v7



func = Model().to('cpu')


x = torch.randn(1, 192)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpnqa4isq2/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpnqa4isq2/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpnqa4isq2', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
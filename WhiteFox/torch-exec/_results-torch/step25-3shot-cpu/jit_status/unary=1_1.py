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
        self.fc1 = torch.nn.Linear(10, 4)
        self.fc2 = torch.nn.Linear(4, 2)
        torch.nn.init.uniform_(self.fc1.weight, -0.005, 0.005)
        torch.nn.init.zeros_(self.fc1.bias)
        torch.nn.init.uniform_(self.fc2.weight, -0.005, 0.005)
        torch.nn.init.zeros_(self.fc2.bias)

    def forward(self, x):
        x = x + x * x * x * 0.044715
        x = torch.tanh(x)
        v1 = self.fc1(x)
        v2 = torch.tanh(v1)
        v3 = v2 + 1
        v4 = self.fc2(v3)
        return v4


func = Model().to('cpu')


x1 = torch.randn(1, 10)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpom3qt_10/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpom3qt_10/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpom3qt_10', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def forward(self, x0, x1):
        v0 = torch.nn.functional.linear(x0, self.linear.weight, self.linear.bias).permute(0, 2, 1)
        lstm1 = torch.nn.LSTMCell(3, 2)
        v1 = lstm1(v0)
        v2 = v1.transpose(0, 1)
        v3 = v2.transpose(0, 1)
        v4 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias).permute(0, 2, 1)
        lstm2 = torch.nn.LSTMCell(3, 2)
        v5 = lstm2(v4)
        v6 = v5.transpose(0, 1)
        v7 = torch.nn.functional.linear(v6, self.linear.weight, self.linear.bias).permute(0, 2, 1)
        linear1 = torch.nn.Linear(2, 2)
        v8 = linear1(v7)
        return v8.permute(0, 2, 1)



func = Model().to('cuda')


x0 = torch.randn(1, 3, 2)

x1 = torch.randn(1, 3, 2)

test_inputs = [x0, x1]

# JIT_FAIL
'''
direct:
LSTMCell: Expected input to be 1D or 2D, got 3D instead

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp8ez3zn10/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp8ez3zn10/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp8ez3zn10', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
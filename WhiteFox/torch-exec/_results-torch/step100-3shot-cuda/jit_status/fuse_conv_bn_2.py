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
        torch.manual_seed(4)
        self.linear1 = torch.nn.Linear(20, 10)
        torch.manual_seed(3)
        self.linear1_bn = torch.nn.BatchNorm1d(10)
        self.relu = torch.nn.ReLU()
        torch.manual_seed(2)
        self.linear2 = torch.nn.Linear(10, 10)
        torch.manual_seed(1)
        self.linear2_bn = torch.nn.BatchNorm1d(10)

    def forward(self, x1):
        y1 = self.linear1(x1)
        y1 = self.linear1_bn(y1)
        y1 = self.relu(y1)
        y1 = self.linear2(y1)
        y1 = self.linear2_bn(y1)
        return y1



func = Model().to('cuda')


x1 = torch.randn(1, 20)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpog9dee9_/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpog9dee9_/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpog9dee9_', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
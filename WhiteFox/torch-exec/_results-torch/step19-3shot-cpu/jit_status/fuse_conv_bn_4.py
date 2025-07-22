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
        s = torch.nn.Sequential(torch.nn.Conv2d(1, 3, 2, bias=False), torch.nn.BatchNorm2d(3), torch.nn.Conv2d(3, 4, 2, bias=False))
        torch.manual_seed(3)
        s[0].weight = torch.nn.Parameter(torch.randn(s[0].weight.shape))
        torch.manual_seed(4)
        s[2].weight = torch.nn.Parameter(torch.randn(s[2].weight.shape))
        self.layer = s

    def forward(self, x1):
        s1 = self.layer(x1)
        return s1



func = Model().to('cpu')


x1 = torch.randn(1, 1, 4, 4)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmplir7orhb/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmplir7orhb/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmplir7orhb', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
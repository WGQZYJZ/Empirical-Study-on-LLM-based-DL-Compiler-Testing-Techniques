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
        super(Model, self).__init__()
        a = torch.nn.modules.ModuleList([torch.nn.Conv2d(2, 2, 3) for _ in range(3)])
        torch.manual_seed(3)
        a[1].weight = torch.nn.Parameter(torch.randn(a[1].weight.shape))
        torch.manual_seed(4)
        a[2].weight = torch.nn.Parameter(torch.randn(a[2].weight.shape))
        torch.manual_seed(5)
        a[1].bias = torch.nn.Parameter(torch.randn(a[1].bias.shape))
        torch.manual_seed(6)
        a[2].bias = torch.nn.Parameter(torch.randn(a[2].bias.shape))
        self.layer = a

    def forward(self, x1):
        s1 = self.layer[1](x1)
        t1 = self.layer[2](x1)
        return s1 + t1



func = Model().to('cpu')


x1 = torch.randn(1, 2, 4, 4)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpeduiiqe2/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpeduiiqe2/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpeduiiqe2', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
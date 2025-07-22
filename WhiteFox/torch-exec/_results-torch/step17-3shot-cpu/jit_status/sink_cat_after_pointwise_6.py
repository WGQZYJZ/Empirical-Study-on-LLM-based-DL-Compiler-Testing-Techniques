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

class ModelA(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x, y):
        z0 = torch.cat((x, y), dim=1)
        out = self.relu(z0)
        out = out.view(-1)
        out = self.relu(out)
        out = out.view(-1)
        return out

class ModelB(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        z0 = torch.cat((x, y), dim=1)
        z1 = z0.permute((1, 0, 2)).reshape(z0.shape[0], -1)
        z2 = torch.relu(z1)
        z3 = z2.view(z2.shape[0], 1, z2.shape[1]).permute(1, 0, 2)
        out = torch.cat((z3, z3), dim=1)
        return out


func = ModelB().to('cpu')


x = torch.randn(2, 3, 4)

y = torch.randn(2, 3, 4)

test_inputs = [x, y]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpcxzc9yyv/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpcxzc9yyv/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpcxzc9yyv', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
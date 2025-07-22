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
        self.layer0 = torch.nn.Sequential(torch.nn.Conv2d(3, 32, 1, 1, bias=False), torch.nn.GroupNorm(2, 32), torch.nn.ReLU(), torch.nn.Conv2d(32, 32, 3, 2, 1, bias=False))
        self.layer1 = torch.nn.Sequential(torch.nn.Conv2d(32, 64, 1, 1, bias=False), torch.nn.GroupNorm(2, 64), torch.nn.ReLU(), torch.nn.Conv2d(64, 32, 1, 1, bias=False), torch.nn.GroupNorm(2, 32), torch.nn.ReLU(), torch.nn.Conv2d(32, 32, 3, 2, 1, bias=False))
        self.layer2 = torch.nn.Sequential(torch.nn.Conv2d(32, 32, 1, 1, bias=False), torch.nn.GroupNorm(2, 32), torch.nn.ReLU(), torch.nn.Conv2d(32, 32, 3, 1, bias=False))
        self.layer3 = torch.nn.Sequential(torch.nn.Conv2d(32, 1, 1, 1, bias=True))

    def forward(self, inputs):
        x1 = self.layer0(inputs)
        x2 = self.layer1(x1)
        x3 = self.layer2(x2)
        y1 = self.layer3(x3)
        x1 = x1.view(x1.size()[0], -1)
        x2 = x2.view(x2.size()[0], -1)
        x3 = x3.view(x3.size()[0], -1)
        y1 = y1.view(y1.size()[0], -1)
        z1 = torch.cat((x1, x2, y1), dim=1)
        return z1



func = Model().to('cpu')


x1 = torch.randn(1, 3, 96, 96)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpya8uo7ix/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpya8uo7ix/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpya8uo7ix', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
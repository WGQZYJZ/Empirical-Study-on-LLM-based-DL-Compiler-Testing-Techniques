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
        self.conv1 = torch.nn.Conv2d(1, 20, 5, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(20, 50, 5, stride=1, padding=0)
        self.fc1 = torch.nn.Linear(800, 500)
        self.fc2 = torch.nn.Linear(500, 10)

    def forward(self, x1):
        t1 = self.conv1(x1)
        t2 = self.conv2(t1)
        t3 = t2.view(-1, 800)
        t4 = torch.nn.Tanh(self.fc1(t3))
        t5 = torch.nn.ReLU6(self.fc2(t4))
        t6 = t5 / 6
        return t6.unsqueeze(-1)



func = Model().to('cpu')


x1 = torch.randn(1, 1, 28, 28)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Tanh.__init__() takes 1 positional argument but 2 were given

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp92xbtgg_/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp92xbtgg_/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp92xbtgg_', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
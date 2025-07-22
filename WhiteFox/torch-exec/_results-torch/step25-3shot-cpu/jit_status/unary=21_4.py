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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super(ModelTanh, self).__init__()
        self.conv1 = torch.nn.Conv2d(3, 30, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(30, 54, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(54, 30, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(30, 10, 1, stride=1, padding=0)
        self.tanh = torch.nn.Tanh()

    def forward(self, x):
        v1 = self.conv1(x)
        v1 = self.tanh(v1)
        v2 = self.conv2(v1)
        v2 = self.tanh(v2)
        v3 = self.conv3(v2)
        v3 = self.tanh(v3)
        v4 = self.conv4(v3)
        v4 = self.tanh(v4)
        return v4



func = ModelTanh().to('cpu')


x = torch.randn(1, 3, 60, 60)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp6nr5jlso/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp6nr5jlso/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp6nr5jlso', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(3, 64, 3, padding=1, stride=1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(64, 64, 3, padding=1, stride=2)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(64, 64, 3, padding=1, stride=1)
        self.conv_transpose4 = torch.nn.ConvTranspose2d(64, 9, 3, padding=1, stride=2)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = F.relu(v1)
        v3 = self.conv_transpose2(v2)
        v4 = F.relu(v3)
        v5 = self.conv_transpose3(v4)
        v6 = F.relu(v5)
        v7 = self.conv_transpose4(v6)
        return v7



func = Model().to('cpu')


x1 = torch.randn(4, 3, 128, 128)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpzaumsav6/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpzaumsav6/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpzaumsav6', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
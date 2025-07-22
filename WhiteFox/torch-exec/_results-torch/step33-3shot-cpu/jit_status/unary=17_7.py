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
        self.conv_transpose = nn.ConvTranspose2d(3, 64, kernel_size=2, stride=2)
        self.conv_transpose1 = nn.ConvTranspose2d(64, 16, kernel_size=2, stride=2)
        self.conv_transpose2 = nn.ConvTranspose2d(16, 4, kernel_size=2, stride=1)

    def forward(self, x):
        x = self.conv_transpose(x)
        x = torch.relu(x)
        x = self.conv_transpose1(x)
        x = torch.relu(x)
        x = self.conv_transpose2(x)
        return x



func = Model().to('cpu')


W_in = 16
H_in = 16
C_in = 3
N = 1
x = torch.randn(N, C_in, H_in, W_in)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp7nkfeaq0/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp7nkfeaq0/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp7nkfeaq0', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
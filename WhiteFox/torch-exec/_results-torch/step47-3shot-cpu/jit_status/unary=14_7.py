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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(3, 256, 1, stride=1, padding=0)
        self.conv_transpose_1_1 = torch.nn.ConvTranspose2d(256, 256, 1, stride=1, padding=0)
        self.conv_transpose_1_2 = torch.nn.ConvTranspose2d(256, 64, 3, stride=1, padding=1)
        self.conv_transpose_1_3 = torch.nn.ConvTranspose2d(64, 3, 3, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv_transpose_1(x)
        v1_1 = self.conv_transpose_1_1(v1)
        v1_2 = self.conv_transpose_1_2(v1_1)
        v1_3 = self.conv_transpose_1_3(v1_2)
        v3 = torch.sigmoid(v1_3)
        v5 = v1_3 * v3
        return v5



func = Model().to('cpu')


x = torch.randn(1, 3, 512, 512)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpf52eztb6/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpf52eztb6/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpf52eztb6', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
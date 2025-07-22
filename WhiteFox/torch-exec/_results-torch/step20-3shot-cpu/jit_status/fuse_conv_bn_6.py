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

class LayerWiseModel(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 3, padding=1)
        self.conv2 = torch.nn.Conv2d(64, 32, 3, padding=1)
        self.conv3 = torch.nn.Conv2d(32, 16, 3, padding=1)
        self.conv4 = torch.nn.Conv2d(16, 3, 3, padding=1)

    def forward(self, x1, x2, x3, x4):
        y1 = self.conv1(x1)
        y2 = self.conv2(y1)
        y3 = self.conv3(y2)
        y4 = self.conv4(y3)
        return (y1, y2, y3, y4)



func = LayerWiseModel().to('cpu')


x1 = torch.randn(1, 3, 10, 10)

x2 = torch.randn(1, 32, 6, 6)

x3 = torch.randn(1, 16, 4, 4)

x4 = torch.randn(1, 3, 2, 2)

test_inputs = [x1, x2, x3, x4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmps3hfpi_r/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmps3hfpi_r/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmps3hfpi_r', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
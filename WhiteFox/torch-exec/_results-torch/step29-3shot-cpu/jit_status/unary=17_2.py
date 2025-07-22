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
        self.conv1 = torch.nn.ConvTranspose2d(1, 16, (4, 3), padding=(1, 0), stride=(2, 1))
        self.conv2 = torch.nn.ConvTranspose2d(16, 8, (3, 5), padding=(1, 1), stride=(2, 1))
        self.conv3 = torch.nn.ConvTranspose2d(8, 1, (2, 4), padding=(0, 0), stride=(3, 1))

    def forward(self, x):
        x1 = self.conv1(x)
        x1 = F.relu(x1)
        x2 = self.conv2(x1)
        x2 = F.relu(x2)
        x3 = self.conv3(x2)
        return x3



func = Model().to('cpu')


x = torch.randn(1, 1, 30, 10)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmphxiu8ujj/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmphxiu8ujj/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmphxiu8ujj', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
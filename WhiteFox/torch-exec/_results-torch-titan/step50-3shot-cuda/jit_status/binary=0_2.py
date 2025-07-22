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
        self.conv = torch.nn.Conv2d(3, 8, 3, stride=1, padding=3)

    def forward(self, x1, other, y, padding1, padding2=None):
        v1 = self.conv(x1)
        if (padding2 == None):
            padding2 = torch.randn(v1.shape)
        v2 = (v1 + other)
        v3 = (y + v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)

other = 1
y = 1
padding1 = 1

test_inputs = [x1, other, y, padding1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp82wi78w7/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp82wi78w7', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp82wi78w7/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
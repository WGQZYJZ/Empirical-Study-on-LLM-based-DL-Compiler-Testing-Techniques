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
        self.conv = torch.nn.ConvTranspose3d(3, 16, 2, stride=2)
        self.conv1 = torch.nn.ConvTranspose3d(16, 32, 2, stride=2)
        self.conv2 = torch.nn.ConvTranspose3d(32, 1, 2, stride=2)

    def forward(self, x):
        v = self.conv(x)
        v1 = self.conv1(v)
        v2 = self.conv2(v1)
        return v2




func = Model().to('cuda')



x = torch.randn(1, 3, 8, 8, 8)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpnexscpi0/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpnexscpi0', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpnexscpi0/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
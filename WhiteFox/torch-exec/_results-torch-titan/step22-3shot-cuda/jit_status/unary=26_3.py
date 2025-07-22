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

    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.Conv2d(49, 1, 3, stride=3)
        self.conv_t = torch.nn.ConvTranspose2d(1, 1, 2, stride=2)
        self.negative_slope = negative_slope

    def forward(self, x):
        y = self.conv(x)
        z = self.conv_t(y)
        m = (z > 0)
        n = (z * self.negative_slope)
        o = torch.where(m, z, n)
        return o




negative_slope = 5.398


func = Model(negative_slope).to('cuda')



x = torch.randn(1, 49, 8, 8)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpgpnb6o5o/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpgpnb6o5o', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpgpnb6o5o/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
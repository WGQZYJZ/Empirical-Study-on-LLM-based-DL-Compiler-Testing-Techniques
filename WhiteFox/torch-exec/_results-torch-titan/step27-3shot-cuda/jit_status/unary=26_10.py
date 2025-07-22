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
        self.conv = torch.nn.Conv2d(36, 50, 1, stride=1)
        self.conv_t4 = torch.nn.ConvTranspose2d(50, 1, 2, stride=2)
        self.conv_t5 = torch.nn.ConvTranspose2d(1, 1, 1, stride=1)
        self.conv_t6 = torch.nn.ConvTranspose2d(1, 1, 4, stride=4)
        self.conv_t7 = torch.nn.ConvTranspose2d(1, 1, 8, stride=8)

    def forward(self, x):
        y = self.conv(x)
        z1 = self.conv_t4(y)
        z2 = self.conv_t5(z1)
        z3 = self.conv_t6(z2)
        z4 = self.conv_t7(z3)
        return z4




func = Model().to('cuda')



x = torch.randn(1, 36, 32, 32)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpdutcrq5n/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpdutcrq5n', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpdutcrq5n/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
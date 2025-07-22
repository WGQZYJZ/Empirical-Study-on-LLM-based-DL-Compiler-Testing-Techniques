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
        self.c4 = torch.nn.ConvTranspose2d(128, 64, kernel_size=1)
        self.c8 = torch.nn.ConvTranspose2d(64, 32, kernel_size=1)
        self.c16 = torch.nn.ConvTranspose2d(32, 4, kernel_size=1)
        self.c32 = torch.nn.ConvTranspose2d(4, 1, kernel_size=1)

    def forward(self, x):
        x = self.c4(x)
        x = self.c8(x)
        x = self.c16(x)
        x = self.c32(x)
        return x




func = Model().to('cuda')



x1 = torch.randn(1, 128, 2, 2)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmppmjzu50l/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmppmjzu50l', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmppmjzu50l/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
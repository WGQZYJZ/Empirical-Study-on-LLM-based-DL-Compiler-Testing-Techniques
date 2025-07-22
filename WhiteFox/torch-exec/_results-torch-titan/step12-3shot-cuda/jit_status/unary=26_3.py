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
        self.conv_t2 = torch.nn.ConvTranspose2d(1, 2, 1)
        self.conv_t3 = torch.nn.ConvTranspose2d(2, 3, 1)
        self.conv_t4 = torch.nn.ConvTranspose2d(3, 4, 1)

    def forward(self, x):
        x1 = self.conv_t2(x)
        x2 = self.conv_t3(x1)
        x3 = self.conv_t4(x2)
        x4 = (x3 > 0)
        x5 = (x3 * 1.0)
        x6 = torch.where(x4, x3, x5)
        return x6




func = Model().to('cuda')



x = torch.randn(16, 1, 16, 16)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpx6c1_e16/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpx6c1_e16', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpx6c1_e16/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
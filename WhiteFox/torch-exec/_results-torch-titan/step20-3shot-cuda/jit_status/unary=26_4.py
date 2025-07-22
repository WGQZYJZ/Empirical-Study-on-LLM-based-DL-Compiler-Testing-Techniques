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
        self.negative_slope = negative_slope
        self.conv_t1 = torch.nn.ConvTranspose2d(768, 624, 3, stride=1, dilation=3, padding=3)
        self.conv_t2 = torch.nn.ConvTranspose2d(624, 768, 1, stride=1)
        self.conv_t3 = torch.nn.ConvTranspose2d(768, 768, 3, stride=2)

    def forward(self, x1):
        x2 = self.conv_t1(x1)
        x3 = self.conv_t2(x2)
        x4 = self.conv_t3(x3)
        x5 = (x4 > 0)
        x6 = (x4 * self.negative_slope)
        x7 = torch.where(x5, x4, x6)
        return x7




negative_slope = 0.1


func = Model(negative_slope).to('cuda')



x1 = torch.randn(16, 768, 56, 56)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpb8rc73qr/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpb8rc73qr', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpb8rc73qr/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
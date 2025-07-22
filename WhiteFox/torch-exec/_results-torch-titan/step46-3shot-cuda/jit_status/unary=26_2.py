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
        self.conv_t = torch.nn.ConvTranspose2d(61, 72, 2, stride=2, padding=1, bias=False)
        self.bn1 = torch.nn.BatchNorm2d(72)

    def forward(self, x86):
        z86 = self.conv_t(x86)
        z87 = self.bn1(z86)
        z88 = (z87 > 0)
        z89 = (z87 * (- 1.089))
        z90 = torch.where(z88, z87, z89)
        return z90




func = Model().to('cuda')



x86 = torch.randn(1, 61, 87, 33)


test_inputs = [x86]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpplea8woy/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpplea8woy', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpplea8woy/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
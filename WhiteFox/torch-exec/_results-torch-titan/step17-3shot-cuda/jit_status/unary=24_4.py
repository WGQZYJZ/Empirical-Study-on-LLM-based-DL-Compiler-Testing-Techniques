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



class FusionConvBlock(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(4, 8, 3, stride=2, padding=1, dilation=1, groups=2)
        self.conv2 = torch.nn.Conv2d(4, 8, 3, stride=2, padding=1, dilation=1, groups=2)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = (v1 > 0)
        v3 = (v1 * 0.1)
        v4 = self.conv2(x)
        v5 = (v4 > 0)
        v6 = (v4 * 0.1)
        v7 = torch.where(v2, v1, v3)
        return v7




func = FusionConvBlock().to('cuda')



x1 = torch.randn(1, 4, 32, 32)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp9wyewfer/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp9wyewfer', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp9wyewfer/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
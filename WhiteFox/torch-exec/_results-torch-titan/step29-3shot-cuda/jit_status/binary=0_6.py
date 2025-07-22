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
        self.conv = torch.nn.Conv2d(1, 7, 2, stride=2, padding=2)

    def forward(self, x1, other=1, padding1=None, padding2=None, padding3=None, padding4=None, padding5=None):
        v1 = self.conv(x1)
        if (padding1 == None):
            padding1 = torch.randn(v1.shape)
        if (padding2 == None):
            padding2 = torch.randn(v1.shape)
        if (padding3 == None):
            padding3 = torch.randn(v1.shape)
        if (padding4 == None):
            padding4 = torch.randn(v1.shape)
        if (padding5 == None):
            padding5 = torch.randn(v1.shape)
        v2 = (v1 + other)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 1, 7, 7)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpzhy1wp44/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpzhy1wp44', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpzhy1wp44/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
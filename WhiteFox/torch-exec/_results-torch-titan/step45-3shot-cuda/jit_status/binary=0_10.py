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
        self.conv = torch.nn.Conv2d(12, 7, 1, stride=1, padding=1)

    def forward(self, x1, other=0.1, padding1=None, padding2=None, padding3=None, other1=0.1):
        v1 = self.conv(x1)
        if (padding1 == None):
            padding1 = torch.randn(v1.shape)
        if (padding2 == None):
            padding2 = torch.randn(v1.shape)
        if (padding3 == None):
            padding3 = torch.randn(v1.shape)
        v2 = (v1 + other)
        v3 = (v2 + 0.1)
        v4 = (v3 + 0.1)
        v5 = (v4 + 0.1)
        v6 = (v5 + 0.1)
        v7 = (v6 + other1)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 12, 20, 20)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpqos_39_t/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpqos_39_t', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpqos_39_t/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
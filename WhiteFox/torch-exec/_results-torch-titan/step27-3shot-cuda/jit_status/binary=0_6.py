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
        self.conv1 = torch.nn.Conv2d(3, 7, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(7, 8, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(8, 2, 1, stride=1, padding=1)

    def forward(self, x1, other=1, padding1=None, padding2=None):
        var1 = self.conv1(x1)
        if (not (None in (padding1, padding2))):
            var1 += padding1
            var1 -= padding2
        var2 = self.conv2(var1)
        if (not (None in (padding1, padding2))):
            var2 += padding1
        v4 = self.conv3(var2)
        v2 = (v4 + other)
        return var3




class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 7, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(7, 8, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(8, 2, 1, stride=1, padding=1)

    def forward(self, x1, other=1, padding1=None, padding2=None):
        var1 = self.conv1(x1)
        if (not (None in (padding1, padding2))):
            var1 = (var1 + padding1)
            var1 = (var1 + padding2)
        var2 = self.conv2(var1)
        if (not (None in (padding1, padding2))):
            var2 = (var2 - padding1)
            var2 += padding2
        var3 = self.conv3(var2)
        v2 = (var3 + other)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpzmy2u3mq/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpzmy2u3mq', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpzmy2u3mq/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
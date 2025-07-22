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

    def __init__(self, min, max):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 16, 3, stride=2, padding=1, dilation=1, groups=1, bias=False)
        self.maxpool = torch.nn.MaxPool2d(2, stride=2)
        self.conv2 = torch.nn.Conv2d(16, 32, 3, stride=2, padding=1, dilation=1, groups=1, bias=False)
        self.min = min
        self.max = max

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.maxpool(v1)
        v3 = self.conv2(v2)
        v4 = torch.clamp_min(v3, self.min)
        v5 = torch.clamp_max(v4, self.max)
        return v5




min = 100


max = 100


func = Model(min, max).to('cuda')



x1 = torch.randn(1, 1, 100, 100)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpny1_j05i/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpny1_j05i', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpny1_j05i/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
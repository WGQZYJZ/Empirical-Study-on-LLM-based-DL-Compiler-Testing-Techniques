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
        self.conv = torch.nn.Conv2d(1, 2, 1, padding=2, bias=True)
        self.max = max
        self.min = min

    def forward(self, x1):
        v1 = F.conv2d(x1, self.conv.weight, bias=self.conv.bias, groups=self.conv.groups, padding=self.conv.padding, dilation=self.conv.dilation, stride=self.conv.stride)
        v2 = torch.clamp_max(v1, self.max)
        v3 = torch.clamp_min(v2, self.min)
        return v3




min = (- 1.0)


max = 0.9


func = Model(min, max).to('cuda')



x1 = torch.randn(1, 1, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmppp87f374/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmppp87f374', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmppp87f374/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv2d = torch.nn.Conv2d(3, 64, 5, stride=3, padding=1)
        self.min = min
        self.max = max

    def forward(self, x):
        v1 = torch.clamp_min(x, self.min)
        v2 = self.conv2d(v1)
        v3 = torch.clamp_max(v2, self.max)
        s1 = torch.sum(v3)
        v4 = torch.clamp(s1, self.min, self.max)
        return v4




min = 1


max = 3


func = Model(min, max).to('cuda')



x = torch.randn(6, 3, 28, 28)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp8mfyhv40/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp8mfyhv40', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp8mfyhv40/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
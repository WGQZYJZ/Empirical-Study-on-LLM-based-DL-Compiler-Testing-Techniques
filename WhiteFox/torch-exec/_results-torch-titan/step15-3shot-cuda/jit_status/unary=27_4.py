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
        self.conv = torch.nn.Conv2d(9, 20, 5, stride=1, padding=1)
        self.min = min
        self.max = max

    def forward(self, x1):
        conv = self.conv(x1)
        clamp_min = torch.clamp(conv, min=self.min)
        clamp_max = torch.clamp(clamp_min, max=self.max)
        return clamp_max




min = 0.0


max = 0.0


func = Model(min, max).to('cuda')



x1 = torch.randn(1, 9, 32, 32)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpctuvm4h_/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpctuvm4h_', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpctuvm4h_/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
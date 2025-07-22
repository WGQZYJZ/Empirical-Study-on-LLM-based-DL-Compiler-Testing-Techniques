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

    def __init__(self, min_value, max_value):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)
        self.avgpool = torch.nn.AvgPool2d(3, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = self.avgpool(t1)
        t3 = torch.clamp_min(t2, self.min_value)
        t4 = torch.clamp_max(t3, self.max_value)
        return t4




min_value = 0.77


max_value = 0.8


func = Model(min_value, max_value).to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_86yg7mj/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp_86yg7mj', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp_86yg7mj/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
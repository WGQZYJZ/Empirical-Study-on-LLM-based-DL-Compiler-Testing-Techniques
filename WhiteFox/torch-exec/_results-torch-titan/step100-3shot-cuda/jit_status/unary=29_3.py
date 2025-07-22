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

    def __init__(self, min_value=0.4417, max_value=0.8038):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 3, 5, stride=3, padding=2)
        self.conv = torch.nn.Conv2d(3, 3, 5, stride=3, padding=2)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(3, 3, 5, stride=2, padding=2)
        self.conv2 = torch.nn.Conv2d(3, 2, 5, stride=1, padding=2)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.conv(v3)
        v5 = self.conv_transpose2(v4)
        v6 = torch.clamp_min(v5, self.min_value)
        v7 = torch.clamp_max(v6, self.max_value)
        v8 = self.conv2(v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 1, 59, 59)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpe0xv0_fv/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpe0xv0_fv', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpe0xv0_fv/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
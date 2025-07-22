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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(3, 8, 10, stride=1, padding=5)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(8, 6, 15, stride=1, padding=2)
        self.conv_transpose_3 = torch.nn.ConvTranspose2d(6, 4, 15, stride=1, padding=2)
        self.conv_transpose_4 = torch.nn.ConvTranspose2d(4, 2, 10, stride=1, padding=5)

    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        v2 = self.conv_transpose_2(v1)
        v3 = self.conv_transpose_3(v2)
        v4 = self.conv_transpose_4(v3)
        v5 = (v4 + 3)
        v6 = torch.clamp_min(v5, 0)
        v7 = torch.clamp_max(v6, 6)
        v8 = (v7 / 6)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp5wd18eb3/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp5wd18eb3', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp5wd18eb3/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
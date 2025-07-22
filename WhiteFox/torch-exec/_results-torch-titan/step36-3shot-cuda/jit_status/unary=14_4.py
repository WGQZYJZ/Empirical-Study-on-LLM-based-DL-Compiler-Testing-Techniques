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
        self.conv_transpose_0 = torch.nn.ConvTranspose2d(32, 121, 3, stride=1, padding=1)
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(121, 85, 3, stride=1, padding=1)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(85, 56, 3, stride=1, padding=1)
        self.conv_transpose_3 = torch.nn.ConvTranspose2d(56, 42, 3, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose_0(x1)
        v2 = torch.sigmoid(v1)
        v3 = (v1 * v2)
        v4 = self.conv_transpose_1(v3)
        v5 = torch.sigmoid(v4)
        v6 = (v4 * v5)
        v7 = self.conv_transpose_2(v6)
        v8 = torch.sigmoid(v7)
        v9 = (v7 * v8)
        v10 = self.conv_transpose_3(v9)
        v11 = torch.sigmoid(v10)
        v12 = (v10 * v11)
        return v12




func = Model().to('cuda')



x1 = torch.randn(1, 32, 128, 128)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpyqdezd9k/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpyqdezd9k', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpyqdezd9k/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv_transpose_16 = torch.nn.ConvTranspose3d(16, 16, 5, stride=1, padding=1, output_padding=0, dilation=1)
        self.conv_transpose_18 = torch.nn.ConvTranspose3d(16, 16, 5, stride=2, padding=2, output_padding=0, dilation=1)
        self.conv_transpose_20 = torch.nn.ConvTranspose3d(16, 16, 5, stride=2, padding=2, output_padding=(1, 0, 0), dilation=1)
        self.conv_transpose_22 = torch.nn.ConvTranspose3d(16, 16, 5, stride=2, padding=2, output_padding=(1, 1, 1), dilation=1)

    def forward(self, x2):
        v1 = self.conv_transpose_16(x2)
        v2 = torch.sigmoid(v1)
        v3 = (v1 * v2)
        v4 = self.conv_transpose_18(v3)
        v5 = torch.sigmoid(v4)
        v6 = (v4 * v5)
        v7 = self.conv_transpose_20(v6)
        v8 = torch.sigmoid(v7)
        v9 = (v7 * v8)
        v10 = self.conv_transpose_22(v9)
        return v10




func = Model().to('cuda')



x2 = torch.randn(1, 16, 14, 14, 14)


test_inputs = [x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmprszhpea1/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmprszhpea1', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmprszhpea1/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
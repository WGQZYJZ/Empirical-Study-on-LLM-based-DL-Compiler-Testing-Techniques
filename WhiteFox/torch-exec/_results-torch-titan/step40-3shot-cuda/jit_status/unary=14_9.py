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
        self.conv2d_0 = torch.nn.Conv2d(1, 15, 3, stride=2, dilation=1, padding=0)
        self.conv_transpose_0 = torch.nn.ConvTranspose2d(15, 2, 3, stride=1, padding=1, output_padding=0)
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(2, 7, 4, stride=2, dilation=1, padding=0)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(7, 14, 3, stride=1, padding=1)
        self.conv_transpose_3 = torch.nn.ConvTranspose2d(14, 4, 1, stride=1, padding=0)
        self.conv_transpose_4 = torch.nn.ConvTranspose2d(4, 2, 3, stride=1, padding=1)
        self.conv_transpose_5 = torch.nn.ConvTranspose2d(2, 15, 1, stride=1, padding=0)
        self.conv_transpose_6 = torch.nn.ConvTranspose2d(15, 2, 3, stride=1, padding=1)

    def forward(self, x1):
        v0 = self.conv2d_0(x1)
        v1 = torch.sigmoid(v0)
        v2 = (v0 * v1)
        v3 = self.conv_transpose_0(v2)
        v4 = torch.sigmoid(v3)
        v5 = (v3 * v4)
        v6 = self.conv_transpose_1(v5)
        v7 = torch.sigmoid(v6)
        v8 = (v6 * v7)
        v9 = self.conv_transpose_2(v8)
        v10 = torch.sigmoid(v9)
        v11 = (v9 * v10)
        v12 = self.conv_transpose_3(v11)
        v13 = torch.sigmoid(v12)
        v14 = (v12 * v13)
        v15 = self.conv_transpose_4(v14)
        v16 = torch.sigmoid(v15)
        v17 = (v15 * v16)
        v18 = self.conv_transpose_5(v17)
        v19 = torch.sigmoid(v18)
        v20 = (v18 * v19)
        v21 = self.conv_transpose_6(v20)
        return v21




func = Model().to('cuda')



x1 = torch.randn(1, 1, 28, 28)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp35z51_he/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp35z51_he', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp35z51_he/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv_transpose_7 = torch.nn.ConvTranspose3d(2, 40, 6, stride=3, padding=2)
        self.conv_transpose_9 = torch.nn.ConvTranspose3d(40, 20, 7, stride=2, padding=2)
        self.conv_transpose_11 = torch.nn.ConvTranspose3d(20, 5, 12, stride=6, padding=4)
        self.conv_transpose_13 = torch.nn.ConvTranspose3d(5, 1, 2, stride=3, padding=2)

    def forward(self, x1):
        v1 = self.conv_transpose_7(x1)
        v2 = torch.sigmoid(v1)
        v3 = (v1 * v2)
        v4 = self.conv_transpose_9(v3)
        v5 = torch.sigmoid(v4)
        v6 = (v4 * v5)
        v7 = self.conv_transpose_11(v6)
        v8 = torch.sigmoid(v7)
        v9 = (v7 * v8)
        v10 = self.conv_transpose_13(v9)
        return v10




func = Model().to('cuda')



x1 = torch.randn(1, 2, 8, 8, 8)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpzh0l9ebk/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpzh0l9ebk', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpzh0l9ebk/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
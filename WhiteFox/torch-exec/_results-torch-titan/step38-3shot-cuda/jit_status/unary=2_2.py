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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(1, 4, 7, stride=2, padding=1)
        self.conv_transpose_1_pointwise = torch.nn.Conv2d(4, 4, 1)
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(4, 8, 4, stride=(2, 2), padding=1)
        self.conv_transpose_2_pointwise = torch.nn.Conv2d(8, 8, 1)
        self.conv_transpose_3 = torch.nn.ConvTranspose2d(8, 1, 4, stride=2)

    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        v2 = self.conv_transpose_1_pointwise(v1)
        v3 = self.conv_transpose_2(v2)
        v4 = self.conv_transpose_2_pointwise(v3)
        v5 = self.conv_transpose_3(v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(5, 1, 24, 33)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpwr5yogbj/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpwr5yogbj', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpwr5yogbj/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

class ConvTranspose3dModel(torch.nn.Module):

    def __init__(self):
        super(ConvTranspose3dModel, self).__init__()
        self.conv_transpose_layer = torch.nn.ConvTranspose3d(43, 47, 4, stride=1, padding=1, output_padding=0, groups=1, bias=True, dilation=2)

    def forward(self, x1):
        x2 = self.conv_transpose_layer(x1)
        x3 = x2 > 0
        x4 = x2 * 0.4
        x5 = torch.where(x3, x2, x4)
        return x5



func = ConvTranspose3dModel().to('cuda')


x6 = torch.randn(1, 43, 7, 11, 14)

test_inputs = [x6]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpjr1ezxzs/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpjr1ezxzs/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpjr1ezxzs', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
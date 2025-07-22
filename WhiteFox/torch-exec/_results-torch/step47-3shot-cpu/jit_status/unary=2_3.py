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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(2048, 512, 4, stride=1, padding=0, output_padding=0, groups=1, bias=True, dilation=1, padding_mode='zeros')
        self.conv_transpose2 = torch.nn.ConvTranspose2d(512, 128, 4, stride=2, padding=1, output_padding=1, groups=1, bias=False, dilation=1, padding_mode='zeros')
        self.conv_transpose3 = torch.nn.ConvTranspose2d(128, 64, 3, stride=2, padding=1, output_padding=0, groups=1, bias=False, dilation=1, padding_mode='zeros')
        self.conv_transpose4 = torch.nn.ConvTranspose2d(64, 1, 8, stride=2, padding=0, output_padding=0, groups=1, bias=False, dilation=1, padding_mode='zeros')

    def forward(self, *args, **kwargs):
        v1 = self.conv_transpose1(*args, **kwargs)
        v2 = self.conv_transpose2(v1)
        v3 = self.conv_transpose3(v2)
        v4 = self.conv_transpose4(v3) + 0.5
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 2048, 50, 50)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_obr4f55/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp_obr4f55/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp_obr4f55', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv = torch.nn.ConvTranspose2d(in_channels=24, out_channels=11, kernel_size=(3, 7), padding=(1, 3), output_padding=(0, 1))

    def forward(self, input):
        v1 = self.conv(input)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7978845608028654)
        v4 = torch.tanh(v3)
        v5 = (v4 * 0.044715)
        v6 = torch.mul(v2, v1)
        v7 = (v6 * v2)
        v8 = (v5 * v7)
        o = (v2 + v8)
        return o



func = Model().to('cuda')



x = torch.randn(1, 24, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_height: 0 output_padding_width: 1 stride_height: 1 stride_width: 1 dilation_height: 1 dilation_width: 1

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp4nxzclom/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp4nxzclom', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp4nxzclom/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
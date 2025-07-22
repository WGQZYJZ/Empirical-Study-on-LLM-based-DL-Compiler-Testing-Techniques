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
        self.conv_t1 = torch.nn.ConvTranspose2d(64, 32, kernel_size=(2, 2), stride=(2, 2), dilation=(1, 1), padding=(0, 0), output_padding=(0, 0))
        self.conv_t2 = torch.nn.ConvTranspose2d(32, 128, kernel_size=(3, 3), stride=(1, 1), dilation=(2, 2), padding=(2, 2), output_padding=1)
        self.conv_t3 = torch.nn.ConvTranspose2d(128, 64, kernel_size=(2, 2), stride=(1, 1), dilation=(1, 1), padding=(0, 0), output_padding=0)
        self.conv_transpose = torch.nn.ConvTranspose2d(64, 16, kernel_size=(2, 2), stride=(1, 1), dilation=(2, 2), padding=(2, 2))

    def forward(self, x1):
        v1 = self.conv_t1(x1)
        v2 = self.conv_t2(v1)
        v3 = self.conv_t3(v2)
        v4 = self.conv_transpose(v3)
        v5 = v4 * 0.5
        v6 = v4 * v4 * v4
        v7 = v6 * 0.044715
        v8 = v4 + v7
        v9 = v8 * 0.7978845608028654
        v10 = torch.tanh(v9)
        v11 = v10 + 1
        v12 = v5 * v11
        return v12



func = Model().to('cpu')


x1 = torch.randn(1, 64, 32, 32)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpgf6tbhse/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpgf6tbhse/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpgf6tbhse', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.deconv1 = torch.nn.ConvTranspose2d(12, 12, 2, stride=2, output_padding=1)
        self.deconv2 = torch.nn.ConvTranspose2d(12, 4, 1, stride=1)

    def forward(self, x1):
        v1 = self.deconv1(x1)
        v2 = v1 * 0.5
        v3 = v1 * v1 * v1
        v4 = v3 * 0.044715
        v5 = v1 + v4
        v6 = v5 * 0.7978845608028654
        v7 = torch.tanh(v6)
        v8 = v7 + 1
        v9 = v2 * v8
        v12 = self.deconv2(v9)
        v16 = v12 * 0.99867363
        v15 = v12 * v12 * v12
        v14 = v15 * 0.8936171
        v13 = v12 + v14
        v17 = v13 * 0.98326338
        v11 = torch.tanh(v17)
        v10 = v11 + 1
        v18 = v16 * v10
        return v18



func = Model().to('cuda')


x1 = torch.randn(8, 12, 4, 4)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpnm7j6okw/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpnm7j6okw/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpnm7j6okw', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
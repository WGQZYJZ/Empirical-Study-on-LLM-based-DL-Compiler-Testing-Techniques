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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(5, 12, kernel_size=4, stride=2, padding=1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(12, 6, kernel_size=3, stride=3, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = v1 * 0.2689414213699951
        v3 = v1 * 0.5873179595718384
        v4 = v3 * 0.7071067811865476
        v5 = v4 * 0.5590169943749475
        v6 = -1.5707963267948966 == v3
        v7 = v2 * v5
        v8 = torch.tanh(v7)
        v9 = v8 + 1.1240370639648438
        v10 = v1 - v2
        v11 = torch.erf(v10)
        v12 = v11 + 0.7071067811865476
        v13 = v9 * v12
        return v13



func = Model().to('cpu')


x1 = torch.randn(1, 5, 3, 6)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpwtc2tl8v/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpwtc2tl8v/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpwtc2tl8v', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
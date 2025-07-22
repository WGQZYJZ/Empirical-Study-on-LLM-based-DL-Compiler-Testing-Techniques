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

    def __init__(self, max_value=1):
        super().__init__()
        self.conv_transpose1 = torch.nn.ConvTranspose2d(3, 1, 4, stride=4, padding=4)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(1, 1, 3, stride=3, padding=3)
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = torch.clamp_max(v1, self.max_value)
        v3 = self.conv_transpose2(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 3, 128, 128)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp224mlwmw/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp224mlwmw/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp224mlwmw', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
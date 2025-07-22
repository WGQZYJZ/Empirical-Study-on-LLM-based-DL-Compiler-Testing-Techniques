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
        self.conv_t = torch.nn.ConvTranspose2d(455, 287, 8, stride=4, padding=0, bias=True)

    def forward(self, x11):
        h1 = self.conv_t(x11)
        h2 = h1 > 0
        h3 = h1 * -0.0896
        h4 = torch.where(h2, h1, h3)
        return torch.nn.functional.adaptive_avg_pool2d(h4, (1, 1))



func = Model().to('cpu')


x11 = torch.randn(11, 455, 16, 12)

test_inputs = [x11]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmph_mfk74o/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmph_mfk74o/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmph_mfk74o', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
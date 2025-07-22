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
        self.conv_t = torch.nn.ConvTranspose2d(4, 6, 5, padding=2, stride=1)
        self.negative_slope = 0.2

    def forward(self, x3):
        m1 = self.conv_t(x3)
        m2 = m1 > 0
        m3 = m1 * self.negative_slope
        m4 = torch.where(m2, m1, m3)
        return torch.nn.functional.dropout(m4, p=0.3850582905077984, train=False)



func = Model().to('cpu')


x3 = torch.randn(5, 4, 83, 76)

test_inputs = [x3]

# JIT_FAIL
'''
direct:
dropout() got an unexpected keyword argument 'train'

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmptvmoojqt/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmptvmoojqt/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmptvmoojqt', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
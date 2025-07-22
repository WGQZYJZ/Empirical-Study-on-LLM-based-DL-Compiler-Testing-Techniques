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
        self.conv_t = torch.nn.ConvTranspose2d(10, 10, 3, bias=False, padding=(3, 0))

    def forward(self, x4):
        m1 = self.conv_t(x4)
        m2 = m1 > 0
        m3 = m1 * -0.30569046525001525
        m4 = torch.where(m2, m1, m3)
        return torch.nn.functional.conv2d(m4, weight=torch.ones(10, 25, 3, 2), bias=None, stride=(90, 90), padding=None, dilation=1, groups=1)



func = Model().to('cpu')


x4 = torch.randn(27, 10, 88, 22)

test_inputs = [x4]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (Tensor, groups=int, dilation=int, stride=tuple, padding=NoneType, bias=NoneType, weight=Tensor), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, tuple of ints padding = 0, tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the keywords were incorrect: groups, dilation, stride, padding, bias
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, str padding = "valid", tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the keywords were incorrect: groups, dilation, stride, padding, bias


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpuohxrt1i/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpuohxrt1i/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpuohxrt1i', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
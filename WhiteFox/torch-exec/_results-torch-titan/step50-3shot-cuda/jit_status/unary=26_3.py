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
        self.conv_t = torch.nn.ConvTranspose3d(20, 34, kernel_size=(11, 11, 11), stride=(1, 1, 1), padding=(5, 5, 5), bias=False)

    def forward(self, x18):
        v1 = self.conv_t(x18)
        v2 = (v1 > 0)
        v3 = (v1 * 0.04)
        v4 = torch.where(v2, v1, v3)
        return v4




func = Model().to('cuda')



x18 = torch.randn(10, 20, 19, 27, 37)


test_inputs = [x18]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpeg8js5fo/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpeg8js5fo', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpeg8js5fo/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
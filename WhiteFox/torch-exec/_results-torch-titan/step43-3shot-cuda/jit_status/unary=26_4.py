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
        self.conv_t = torch.nn.ConvTranspose2d(256, 126, 7, stride=1, padding=3, bias=False)

    def forward(self, x14):
        l1 = self.conv_t(x14)
        l2 = (l1 > 1e-05)
        l3 = (l1 * 0.0067)
        l4 = torch.where(l2, l1, l3)
        return l4




func = Model().to('cuda')



x14 = torch.randn(4, 256, 23, 34)


test_inputs = [x14]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp0b5m1i5m/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp0b5m1i5m', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp0b5m1i5m/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
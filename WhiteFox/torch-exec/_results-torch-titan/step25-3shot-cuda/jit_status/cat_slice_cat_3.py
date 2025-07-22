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

    def forward(self, x1, x2, x3, x4, x5, x6, x7, x8):
        c1 = torch.cat([x1, x2, x3, x4, x5, x6, x7, x8], dim=1)
        v1 = c1[:, 0:9223372036854775807]
        s1 = v1[:, 0:3]
        c2 = torch.cat([c1, s1], dim=1)
        return c2



func = Model().to('cuda')



x1 = torch.randn(1, 2, 3)



x2 = torch.ones(1, 2, 3)



x3 = torch.randn(1, 2, 3)



x4 = torch.ones(1, 2, 3)



x5 = torch.randn(1, 2, 3)



x6 = torch.randn(1, 2, 3)



x7 = torch.randn(1, 2, 3)



x8 = torch.ones(1, 2, 3)


test_inputs = [x1, x2, x3, x4, x5, x6, x7, x8]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpu3kcl7v4/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpu3kcl7v4', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpu3kcl7v4/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
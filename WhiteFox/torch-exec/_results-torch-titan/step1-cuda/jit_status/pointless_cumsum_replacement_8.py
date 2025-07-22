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
        self.weight_1 = torch.nn.Parameter(torch.rand(2, 3))
        self.weight_2 = torch.nn.Parameter(torch.rand(2, 2))

    def forward(self, x):
        v1 = torch.einsum('ij,jk->ik', x, self.weight_1)
        v2 = torch.full_like(v1, 1)
        v3 = v1.type(torch.float32)
        v4 = v2.type(torch.float32)
        v5 = (v3 + v4)
        v6 = (v2 + v3)
        v7 = (v4 + v5)
        v8 = torch.cumsum(v7, 0)
        return v8



func = Model().to('cuda')



x = torch.randn(2, 2)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpz46sk61s/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpz46sk61s', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpz46sk61s/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
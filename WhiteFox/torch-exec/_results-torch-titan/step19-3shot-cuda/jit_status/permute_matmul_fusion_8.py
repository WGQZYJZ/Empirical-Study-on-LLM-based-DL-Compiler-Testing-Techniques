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
        self.permute2 = torch.Tensor.permute
        self.add = torch.Tensor.__add__

    def forward(self, x1, x2):
        i1 = self.permute2(x1, 1, 2, 0)
        i2 = self.permute2(x2, 0, 2, 1)
        i3 = self.add(i1, i2)
        i4 = self.permute2(i3, 2, 1, 0)
        i5 = self.permute2(x2, 1, 2, 0)
        i6 = self.add(i4, i5)
        v1 = self.permute2(i6, 1, 2, 0)
        v2 = x1.permute(0, 2, 1)
        v3 = x2.permute(0, 2, 1)
        v4 = torch.matmul(v1, v2)
        v5 = torch.matmul(v3, v4)
        v6 = x1.permute(0, 2, 1)
        v7 = (v5 + v6)
        v8 = torch.matmul(v3, v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)



x2 = torch.randn(1, 2, 2)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp7tmx1tho/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp7tmx1tho', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp7tmx1tho/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
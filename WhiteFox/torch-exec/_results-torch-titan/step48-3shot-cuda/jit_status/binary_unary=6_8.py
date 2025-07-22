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

    def __init__(self, n):
        if ((n < 0) or (not isinstance(n, int))):
            raise ValueError("'n' must be a non-negative integer")
        self.n = math.ceil(n)
        super().__init__()

    def forward(self, x1):
        x = list()
        out = (torch.ones_like(x1[:, 0, :, :]) * x1[:, 0, :, :].mean())
        x.append(out)
        for i in range(0, self.n):
            out = torch.cos(x1.mean())
            x.append(out)
        return x



n = 1
func = Model(5).to('cuda')



x1 = torch.randn(6, 1, 100, 100)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpbosx0hj3/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpbosx0hj3', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpbosx0hj3/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
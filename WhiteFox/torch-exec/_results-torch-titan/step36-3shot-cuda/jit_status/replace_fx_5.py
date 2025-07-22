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

    def __init__(self, p, d):
        super().__init__()
        self.p = p
        self.d = d

    def forward(self, x1, x2):
        x3 = torch.rand_like(x1)
        x4 = F.dropout(x2, p=self.d)
        if (x3.sum() > self.p):
            x5 = (x3 * x1)
        else:
            x5 = (x4 * x1)
        return x5




p = 0.5


d = 0.5


func = Model(p, d).to('cuda')



x1 = torch.randn(1, 5)



x2 = torch.randn(3, 2, 2)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp7_x80caq/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp7_x80caq', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp7_x80caq/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
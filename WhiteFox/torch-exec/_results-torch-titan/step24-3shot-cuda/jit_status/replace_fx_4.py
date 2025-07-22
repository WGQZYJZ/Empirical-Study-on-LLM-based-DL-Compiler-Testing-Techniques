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



class m1(torch.nn.Module):

    def __init__(self, m2):
        super().__init__()
        self.m2 = m2

    def forward(self, x1):
        x2 = torch.nn.functional.dropout(x1, p=0.1)
        x3 = torch.nn.functional.dropout(x2, p=0.2)
        x4 = self.m2(x3, p1=1)
        return x4




class m2(torch.nn.Module):

    def __init__(self, p1):
        super().__init__()
        self.p1 = p1

    def forward(self, x1, p1):
        x2 = (x1 ** p1)
        x3 = torch.nn.functional.dropout(x2, p=0.5)
        x4 = torch.nn.functional.dropout(x3, p=0.6)
        return x4



p1 = 1

func = m2(p1).to('cuda')



x1 = torch.randn(1, 2, 2)

p1 = 1

test_inputs = [x1, p1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp9xa_2ybw/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp9xa_2ybw', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp9xa_2ybw/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
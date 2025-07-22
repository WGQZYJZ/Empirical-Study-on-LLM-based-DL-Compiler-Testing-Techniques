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
        self.c1 = torch.nn.Conv2d(3, 4, 5)

    def forward(self, x1):
        x2 = torch.randint(0, 10, (1,))
        x3 = (x1 ** x2)
        x4 = torch.nn.functional.dropout(x3)
        x5 = torch.randint(0, 10, (1,))
        x6 = torch.rand_like(x4)
        x7 = self.c1(x6)
        x8 = torch.nn.functional.relu(x7)
        return x8




class m2(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.p1 = torch.rand(1)
        self.p2 = torch.nn.Parameter(torch.randn(1))

    def forward(self, x1):
        x2 = (x1 ** self.p1)
        x3 = torch.nn.functional.dropout(x2)
        x4 = torch.randint(0, 10, (1,))
        x5 = torch.rand_like(x3)
        x6 = (self.p2 + x5)
        return x6




func = m2().to('cuda')



x1 = torch.randn(1, 3, 4)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpuqqg6z7x/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpuqqg6z7x', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpuqqg6z7x/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
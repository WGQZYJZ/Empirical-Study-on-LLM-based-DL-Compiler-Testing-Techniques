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

    def __init__(self):
        super().__init__()
        self.m2 = m2(1)

    def forward(self, x1):
        x2 = self.m2(x1)
        x3 = torch.nn.functional.dropout(x2)
        x3 = (x3 + 1)
        x4 = torch.rand_like(x3)
        return x4




class m2(torch.nn.Module):

    def __init__(self, p1):
        super().__init__()
        self.p1 = p1

    def forward(self, x1):
        x2 = (x1 ** self.p1)
        x3 = torch.randint(0, 9, (1,))
        x4 = torch.nn.functional.dropout(x2)
        return x4



p1 = 1

func = m2(p1).to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp0qgzhhpt/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp0qgzhhpt', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp0qgzhhpt/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
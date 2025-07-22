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

    def __init__(self, p1, p2):
        super().__init__()
        t = torch.nn.Dropout(p1)
        self.dropout1 = torch.nn.Dropout(p2)
        self.dropout2 = t

    def forward(self, x1):
        x2 = self.dropout1(x1)
        x3 = torch.rand_like(x2)
        x4 = self.dropout2(x3)
        return x2




p1 = 1


p2 = 0.6


func = Model(p1, p2).to('cuda')



x1 = torch.randn(3, 3, 3)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp5zjl3ll8/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp5zjl3ll8', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp5zjl3ll8/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
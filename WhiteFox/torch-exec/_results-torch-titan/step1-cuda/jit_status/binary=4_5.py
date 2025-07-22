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

    def __init__(self, otherA=1, otherB=2, otherC=3):
        super().__init__()
        self.linear = torch.nn.Linear(8, 4)

    def forward(self, x, other):
        v1 = self.linear(x)
        v2 = (v1 + other)
        return v2



func = Model(otherA=1, otherB=2, otherC=3).to('cuda')



x = torch.randn(1, 8)



other = torch.tensor([4, 5, 6, 7])


test_inputs = [x, other]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpvukg1mi4/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpvukg1mi4', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpvukg1mi4/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
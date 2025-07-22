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

    def __init__(self, linear):
        super().__init__()
        self.linear = linear

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = (v1 - x2)
        return v2




class WeightedSumLinear(torch.nn.Module):

    def __init__(self, weight):
        super().__init__()
        self.weight = weight

    def forward(self, x):
        v = (x * self.weight).sum()
        return v




class Model(torch.nn.Module):

    def __init__(self, linear):
        super().__init__()
        self.linear1 = linear
        self.linear2 = linear
        self.linear3 = linear

    def forward(self, x1, x2, x3):
        v1 = self.linear1(x1)
        v2 = self.linear2(x2)
        v3 = self.linear3(x3)
        v4 = ((v1 + v2) + v3)
        return v4




linear = WeightedSumLinear(torch.nn.Parameter(torch.tensor([1, 2, 3], dtype=torch.float32)))

func = Model(linear).to('cuda')



x1 = torch.randn(1, 2, 3, 3)



x2 = torch.randn(1, 2, 3, 3)



x3 = torch.randn(1, 2, 3, 3)


test_inputs = [x1, x2, x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp0dashy37/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp0dashy37', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp0dashy37/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def __init__(self, negative_slope=0.01):
        super().__init__()
        self.linear = torch.nn.Linear(50, 10)
        self.negative_slope = negative_slope

    def forward(self, x):
        v1 = self.linear(x)
        v2 = (v1 > 0)
        v3 = (v3 * self.negative_slope)
        v4 = torch.where(v2, v1, v3)
        return v4



func = Model().to('cuda')



x = torch.randn(1, 50)


test_inputs = [x]

# JIT_FAIL
'''
direct:
local variable 'v3' referenced before assignment

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp6fnn0p74/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp6fnn0p74', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp6fnn0p74/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
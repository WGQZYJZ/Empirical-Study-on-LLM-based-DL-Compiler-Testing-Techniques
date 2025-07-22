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

    def __init__(self, linear, negative_slope):
        super().__init__()
        self.linear = linear
        self.negative_slope = negative_slope

    def get_leaky_relu(self):
        return (lambda self: Lambda((lambda x: F.leaky_relu(x, self.negative_slope))))

    def forward(self, x2):
        v1 = self.linear(x2)
        v2 = (v1 > 0)
        v3 = (v1 * self.negative_slope)
        v4 = torch.where(v2, v1, v3)
        return v4




linear = torch.nn.Linear(6, 8, bias=False)


negative_slope = 0.01

func = Model(linear, negative_slope).to('cuda')



x2 = torch.randn(1, 6)


test_inputs = [x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp9l65fmkw/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp9l65fmkw', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp9l65fmkw/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
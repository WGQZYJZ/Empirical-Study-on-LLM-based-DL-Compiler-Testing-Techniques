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

    def __init__(self):
        super().__init__()

    def forward(self, x):
        x2 = (x + 1)
        x3 = torch.rand_like(x2)
        x4 = ((x2 + x3) + 1)
        x5 = (((x3 + x4) + 1) + torch.rand_like(x4))
        x6 = ((x4 + (x5 * x6)) - 1)
        x7 = ((x6 @ (x7[:, None] * x7[None, :])) - 1)
        return x7




func = Model().to('cuda')



x1 = torch.randn(10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
local variable 'x6' referenced before assignment

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp0u0s7bit/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp0u0s7bit', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp0u0s7bit/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
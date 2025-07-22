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



class M(torch.nn.Module):

    def __init__(self):
        super().__init__()
        c = torch.nn.Conv2d(2, 4, 4)
        torch.manual_seed(3)
        c.weight = torch.nn.Parameter(torch.randn(c.weight.shape))
        torch.manual_seed(4)
        c.bias = torch.nn.Parameter(torch.randn(c.bias.shape))
        self.c = c

    def forward(self, x):
        v = self.c(x)
        return v




func = M().to('cuda')



x1 = torch.randn(2, 2, 4, 4)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpruzb357i/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpruzb357i', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpruzb357i/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
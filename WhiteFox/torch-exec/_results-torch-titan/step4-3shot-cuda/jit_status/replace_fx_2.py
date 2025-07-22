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



class model(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x, y):
        v1 = torch.nn.functional.dropout(x, p=0.7)
        w1 = torch.rand_like(x, dtype=torch.float)
        y = (v1 + y)
        w2 = torch.rand_like(x, dtype=torch.float)
        t1 = (y + w1)
        z1 = torch.nn.functional.silu(t1)
        w5 = torch.rand_like(x, dtype=torch.float)
        t2 = (v1 + w2)
        w3 = torch.rand_like(x, dtype=torch.float)
        y1 = (t2 + z1)
        w4 = torch.rand_like(x, dtype=torch.float)
        z2 = (y1 + w3)
        return z2




func = model().to('cuda')



x = torch.randn(1, 3, 2, 2)



y = torch.randn(1, 3, 2, 2)


test_inputs = [x, y]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpof76ihq4/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpof76ihq4', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpof76ihq4/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
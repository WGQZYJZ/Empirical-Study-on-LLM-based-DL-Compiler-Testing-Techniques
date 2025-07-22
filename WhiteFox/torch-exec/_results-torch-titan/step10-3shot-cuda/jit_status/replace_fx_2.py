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
        w1 = torch.nn.functional.dropout(x, p=0.2)
        t2 = torch.rand_like(x, dtype=torch.float)
        y1 = (w1 + t2)
        x = (y1 + x)
        w3 = torch.nn.functional.dropout(x, p=0.9)
        y2 = torch.nn.functional.gelu(w3)
        w2 = torch.rand_like(x, dtype=torch.float)
        t3 = (y2 + w2)
        y = (t3 + x)
        w4 = torch.rand_like(x, dtype=torch.float)
        z1 = (y + w4)
        z2 = torch.nn.functional.silu(z1)
        return z2




func = Model().to('cuda')



x = torch.randn(1, 3, 10)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp233bopz2/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp233bopz2', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp233bopz2/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
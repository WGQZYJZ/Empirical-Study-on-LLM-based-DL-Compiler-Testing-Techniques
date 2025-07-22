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

    def forward(self, x1):
        a = torch.randn(1, 2, 2)
        b = torch.nn.functional.dropout(a, p=0.0, training=True)
        c = torch.nn.functional.dropout(b, p=0.1, training=True)
        d = torch.nn.functional.dropout(c, p=0.0, training=True)
        f = torch.nn.functional.dropout(d, p=0.1, training=True)
        e = torch.rand_like(a)
        g = torch.randn(1)
        h = e - g
        i = torch.nn.functional.dropout(f, p=0.1, training=True)
        j = torch.nn.functional.dropout(h, p=0.1, training=True)
        k = torch.randn(2, 2)
        l = torch.randn(2, 2, 2)
        m = m.unsqueeze(0)
        n = torch.nn.functional.dropout(k, p=0.0)
        o = torch.nn.functional.dropout(l, p=0.0)
        p = torch.rand_like(o)
        q = torch.rand_like(o)
        r = o + o
        s = torch.add(p, r)
        t = torch.add(o, p)
        u = torch.add(t, r)
        v = torch.nn.functional.dropout(v, p=0.0, training=True)
        return torch.nn.functional.dropout(u)



func = Model().to('cuda')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
local variable 'm' referenced before assignment

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpx7d_bki7/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpx7d_bki7/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpx7d_bki7', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
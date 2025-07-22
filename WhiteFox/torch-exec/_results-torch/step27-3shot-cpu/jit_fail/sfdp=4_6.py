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
        self.query = torch.nn.Linear(75, 194, bias=False)
        self.key = torch.nn.Linear(75, 194, bias=False)
        self.value = torch.nn.Linear(75, 75, bias=False)

    def forward(self, x1, x2, x3):
        q = self.query(x1)
        k = self.key(x2)
        v = self.value(x3)
        qk = q @ k.T / np.sqrt(q.size(-1))
        m = torch.zeros((q.size(0), 194, qk.size(-1)), dtype=qk.dtype)
        vmask = v >= 0
        m[vmask] = qk[vmask]
        return m


func = Model().to('cpu')


x1 = torch.randn(1, 194, 75)

x2 = torch.randn(1, 194, 75)

x3 = torch.randn(1, 194, 75)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The shape of the mask [1, 194, 75] at index 0 does not match the shape of the indexed tensor [194, 194, 1] at index 0

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmplyuxudet/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmplyuxudet/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmplyuxudet', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
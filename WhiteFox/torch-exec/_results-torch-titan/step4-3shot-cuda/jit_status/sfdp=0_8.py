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

    def __init__(self, dim=128):
        super().__init__()
        self.key = torch.nn.Linear(dim, dim)
        self.query = torch.nn.Linear(dim, dim)

    def forward(self, v1):
        k = self.key(v1)
        q = self.query(v1)
        inv_scale = math.sqrt(k.shape[(- 1)])
        v2 = (torch.matmul(q, k.transpose((- 2), (- 1))) / inv_scale)
        v3 = v2.softmax(dim=(- 1))
        v4 = torch.matmul(v3, v1)
        return v4



func = Model().to('cuda')



v1 = torch.randn(2, 50, 128)


test_inputs = [v1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp36ifj74j/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp36ifj74j', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp36ifj74j/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
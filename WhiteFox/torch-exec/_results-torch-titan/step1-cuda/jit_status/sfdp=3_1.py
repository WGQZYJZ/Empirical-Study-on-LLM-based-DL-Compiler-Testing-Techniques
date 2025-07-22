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
        self.q = torch.nn.Conv2d(32, 64, 3, stride=1, padding=1)
        self.k = torch.nn.Conv2d(32, 64, 1, stride=1)
        self.v = torch.nn.Conv2d(32, 64, 1, stride=1)
        self.scale_factor = math.sqrt(64)

    def forward(self, x):
        q = self.q(x)
        k = self.k(x)
        v = self.v(x)
        s = (torch.matmul(q, k.transpose((- 2), (- 1))) * self.scale_factor)
        d = torch.nn.functional.dropout(s, 0.5)
        o = torch.matmul(d, v)
        return o



func = Model().to('cuda')



x = torch.randn(1, 32, 16, 16)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpd9g52dvc/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpd9g52dvc', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpd9g52dvc/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
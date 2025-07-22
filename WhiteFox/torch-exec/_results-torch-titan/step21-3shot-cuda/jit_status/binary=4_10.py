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
        self.linear1 = torch.nn.Linear(10, 10, bias=False)
        self.linear2 = torch.nn.Linear(10, 10, bias=False)
        self.bn = torch.nn.BatchNorm1d(10)

    def forward(self, x0):
        v0 = torch.add(self.linear1(x0).mean(dim=(- 1), keepdim=True), self.linear2(x0))
        t0 = v0.transpose((- 1), (- 2))
        v1 = self.bn(t0)
        v2 = v1.transpose((- 1), (- 2))
        return v2



func = Model().to('cuda')



x0 = torch.randn(5, 1, 10)


test_inputs = [x0]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp53qazs6m/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp53qazs6m', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp53qazs6m/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
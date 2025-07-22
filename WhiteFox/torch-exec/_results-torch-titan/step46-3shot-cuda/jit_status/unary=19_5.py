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
        self.linear0 = torch.nn.Linear(192, 64)
        self.linear1 = torch.nn.Linear(64, 32)
        self.linear2 = torch.nn.Linear(32, 16)
        self.linear3 = torch.nn.Linear(16, 8)
        self.linear4 = torch.nn.Linear(8, 1)

    def forward(self, x1):
        v1 = self.linear0(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.linear1(v2)
        v4 = torch.sigmoid(v3)
        v5 = self.linear2(v4)
        v6 = torch.sigmoid(v5)
        v7 = self.linear3(v6)
        v8 = torch.sigmoid(v7)
        v9 = self.linear4(v8)
        v10 = torch.sigmoid(v9)
        return v10



func = Model().to('cuda')



x1 = torch.randn(1, 192)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpcpyn7tt4/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpcpyn7tt4', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpcpyn7tt4/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
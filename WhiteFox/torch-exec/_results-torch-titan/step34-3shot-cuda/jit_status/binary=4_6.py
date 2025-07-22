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
        self.mlp = torch.nn.Linear(16, 32)
        self.linear3 = torch.nn.Linear(32, 32)

    def forward(self, x1, other):
        x2 = self.mlp(x1)
        x3 = self.linear3(x2)
        x4 = (x3 + other)
        return x4



func = Model().to('cuda')



x1 = torch.randn(8, 16)



other = torch.randn(8, 32)


test_inputs = [x1, other]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpl95u7fc4/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpl95u7fc4', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpl95u7fc4/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
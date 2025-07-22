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
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(96, 12)

    def forward(self, x3):
        v7 = self.linear(x3)
        v8 = (v7 * 0.5)
        v9 = (v7 + (((v7 * v7) * v7) * 0.044715))
        v10 = (v9 * 0.7978845608028654)
        v11 = torch.tanh(v10)
        v12 = (v11 + 1)
        v13 = (v8 * v12)
        return v13



func = Model().to('cuda')



x3 = torch.randn(1, 96)


test_inputs = [x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpesb9uftl/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpesb9uftl', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpesb9uftl/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def __init__(self, in_features=3, out_features=1, bias=True):
        super().__init__()
        self.linear = torch.nn.Linear(in_features, out_features, bias)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = (v1 + 1)
        v3 = torch.relu(v2)
        return v3



func = Model(in_features=3, out_features=1, bias=True).to('cuda')



x = torch.randn(1, 3)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmph45475a1/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmph45475a1', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmph45475a1/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear1 = torch.nn.Linear(128, 128)
        self.linear2 = torch.nn.Linear(128, 64)
        self.min_val = min_value
        self.max_val = max_value

    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = torch.clamp(v1, min=self.min_val)
        v3 = torch.clamp(v2, max=self.max_val)
        v4 = self.linear2(v3)
        return v4



min_value = 1
max_value = 1

func = Model(min_value, max_value).to('cuda')



x1 = torch.randn(1, 128)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmphyr7uvds/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmphyr7uvds', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmphyr7uvds/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
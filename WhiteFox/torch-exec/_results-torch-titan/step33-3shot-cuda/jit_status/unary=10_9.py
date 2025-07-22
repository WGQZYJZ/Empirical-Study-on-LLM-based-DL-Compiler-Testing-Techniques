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



class Linear0Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(10, 3, bias=False)
        self.relu = torch.nn.ReLU6()

    def forward(self, x2):
        v7 = self.linear1(x2)
        v8 = (v7 + 3)
        v9 = self.relu(v8)
        return v9




class Linear1Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(10, 3, bias=False)
        self.relu = torch.nn.ReLU6()

    def forward(self, x2):
        v7 = self.linear1(x2)
        v8 = (v7 + 3)
        v9 = self.relu(v8)
        return v9




class LinearModel(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.linear0 = Linear0Model()
        self.linear1 = Linear1Model()

    def forward(self, x2):
        l1 = self.linear0(x2)
        l2 = self.linear1(x2)
        return (l1, l2)



func = LinearModel().to('cuda')



x2 = torch.randn(1, 10)


test_inputs = [x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp321bnwnr/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp321bnwnr', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp321bnwnr/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
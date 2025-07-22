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
        self.dropout1 = torch.nn.Dropout(0.8739)
        self.dropout2 = torch.nn.Dropout(0.2876)
        self.linear1 = torch.nn.Linear(75, 72)
        self.linear2 = torch.nn.Linear(72, 44)
        self.linear3 = torch.nn.Linear(44, 87)

    def forward(self, x1):
        v1 = self.dropout1(x1)
        v2 = self.linear1(v1)
        v3 = torch.relu(v2)
        v4 = self.dropout2(v3)
        v5 = self.linear2(v4)
        v6 = torch.relu(v5)
        v7 = self.linear3(v6)
        v8 = torch.tanh(v7)
        return v8




func = Model().to('cuda')



x1 = torch.randn(4, 75)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpjdhfr5bl/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpjdhfr5bl', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpjdhfr5bl/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
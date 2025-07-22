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
        self.linear1 = torch.nn.Linear(5, 8)
        self.linear2 = torch.nn.Linear(8, 1)

    def forward(self, x0):
        v0 = self.linear1(x0)
        v1 = torch.sigmoid(v0)
        v2 = (v1 * 0.7)
        v3 = (v1 + v2)
        v4 = torch.relu(v3)
        v5 = (v4 + 1.5)
        v6 = torch.softmax(v5, dim=(- 1))
        return (v6, v1, v0)



func = Model().to('cuda')



x0 = torch.randn(1, 5)


test_inputs = [x0]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpqqlnx02k/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpqqlnx02k', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpqqlnx02k/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
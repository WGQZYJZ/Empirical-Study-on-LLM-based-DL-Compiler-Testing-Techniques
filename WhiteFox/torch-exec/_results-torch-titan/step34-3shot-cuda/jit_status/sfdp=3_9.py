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

    def __init__(self, dim0, dim1, dim2):
        super().__init__()
        self.dim0 = dim0
        self.dim1 = dim1
        self.dim2 = dim2

    def forward(self, x0, x1):
        s1 = torch.flatten(x0, start_dim=1)
        s2 = torch.flatten(x1, start_dim=1).transpose(0, 1)
        v3 = torch.matmul(s1, s2)
        v4 = (v3 * 0.5)
        v5 = torch.nn.functional.softmax(v4, dim=(- 1))
        v6 = torch.nn.functional.dropout(v5, p=0.2)
        v7 = torch.matmul(v6, s2.transpose(0, 1))
        return v7



dim0 = 1
dim1 = 1
dim2 = 1
func = Model(128, 1, 70).to('cuda')



x0 = torch.randn(1, 128, 1, 70)



x1 = torch.randn(1, 128, 70, 1)


test_inputs = [x0, x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpwi8n11h0/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpwi8n11h0', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpwi8n11h0/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
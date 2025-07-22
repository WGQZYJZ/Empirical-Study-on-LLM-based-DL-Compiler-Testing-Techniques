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
        self.qkvconv = torch.nn.Conv2d(64, 64, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        k1 = self.qkvconv(x1)
        k2 = self.qkvconv(x2)
        k3 = k1.transpose((- 2), (- 1))
        v1 = (k1 * 0.125)
        v2 = (k2.transpose((- 2), (- 1)) * 0.125)
        v3 = torch.matmul(v1, v2)
        v4 = (v3 * 0.25)
        v5 = (v3 * 0.5)
        v6 = torch.exp(v5)
        v7 = torch.nn.functional.dropout(v6, p=0.25)
        return v7



func = Model().to('cuda')



x1 = torch.randn(1, 64, 64, 64)



x2 = torch.randn(1, 64, 64, 64)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp67ybswe4/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp67ybswe4', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp67ybswe4/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
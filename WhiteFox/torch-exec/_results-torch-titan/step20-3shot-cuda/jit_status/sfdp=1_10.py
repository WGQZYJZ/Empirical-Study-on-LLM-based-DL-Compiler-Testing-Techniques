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
        self.key = torch.nn.Parameter(torch.ones(10, 16))
        self.value = torch.nn.Parameter(torch.ones(10, 16))

    def forward(self, x1):
        x2 = torch.matmul(x1, self.key.transpose((- 2), (- 1)))
        x3 = x2.div((2.0 ** 0.5))
        x4 = torch.nn.functional.softmax(x3, dim=(- 1))
        x5 = torch.nn.functional.dropout(x4, p=0.1)
        x6 = torch.matmul(x5, self.value)
        return x6



func = Model().to('cuda')



x1 = torch.randn(1, 16, 16)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpz0nh_8dj/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpz0nh_8dj', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpz0nh_8dj/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
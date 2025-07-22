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

    def forward(self, x1, x2):
        k = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        v = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        q = torch.matmul(x1, x2.transpose((- 2), (- 1)))
        s = k.mul(0.15)
        t = s.softmax((- 1))
        f = torch.nn.functional.dropout(t, 0.4)
        o = torch.matmul(f, x2)
        return o



func = Model().to('cuda')



x1 = torch.randn(1, 4, 64)



x2 = torch.randn(1, 8, 64)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp0al7x_jb/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp0al7x_jb', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp0al7x_jb/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
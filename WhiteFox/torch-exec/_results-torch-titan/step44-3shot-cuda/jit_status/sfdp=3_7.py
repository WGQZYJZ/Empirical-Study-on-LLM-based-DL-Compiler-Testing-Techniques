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

    def forward(self, t0, t1, t2, t3):
        t4 = torch.matmul(t0, torch.transpose(t1, (- 2), (- 1)))
        t5 = (t4 * t3)
        t6 = torch.nn.functional.softmax(t5, dim=(- 1))
        t7 = torch.nn.functional.dropout(t6, p=0.35)
        t8 = torch.matmul(t7, t2)
        return t8



func = Model().to('cuda')



t0 = torch.randn(8, 10, 1, 64, 64)



t1 = torch.randn(8, 10, 1, 64, 64)



t2 = torch.randn(8, 10, 3, 64, 64)

t3 = 1

test_inputs = [t0, t1, t2, t3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp5a5f2mc4/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp5a5f2mc4', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp5a5f2mc4/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
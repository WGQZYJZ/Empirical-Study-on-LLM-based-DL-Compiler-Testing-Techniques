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

    def forward(self, x1, x2, x3, z1, z2):
        b1 = torch.matmul(x1, x2)
        b2 = torch.mm(x3, z1)
        c = torch.matmul(x3, z2)
        t = ((b1 - b2) + c)
        return t




func = Model().to('cuda')



x1 = torch.randn(5, 5)



x2 = torch.randn(5, 5)



x3 = torch.randn(5, 5)



z1 = torch.randn(5, 5)



z2 = torch.randn(5, 5)


test_inputs = [x1, x2, x3, z1, z2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp08_i28v3/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp08_i28v3', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp08_i28v3/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
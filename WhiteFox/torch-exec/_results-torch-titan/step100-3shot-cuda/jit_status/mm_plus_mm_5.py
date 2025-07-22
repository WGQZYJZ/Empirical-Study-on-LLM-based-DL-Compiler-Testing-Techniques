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

    def forward(self, h, i, g, z):
        T0 = (g * i)
        T1 = (z * g)
        T2 = (i * z)
        T3 = (g * g)
        T4 = (z * g)
        T5 = (z * z)
        T6 = (g * g)
        T7 = (i * i)
        out = T0
        return out




func = Model().to('cuda')



h = torch.randn(2, 2)



i = torch.randn(2, 2)



g = torch.randn(2, 2)



z = torch.randn(2, 2)


test_inputs = [h, i, g, z]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpchwv_7l9/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpchwv_7l9', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpchwv_7l9/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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



class Model(nn.Module):

    def forward(self, A1, A2, A3, A4, A5, A6, A7):
        C = (A3 * A7)
        D = (A6 * A5)
        E = (A4 * D)
        F = (C * E)
        G = (A6 * C)
        H = E.mul(A6)
        J = ((F + G) + H)
        return J




func = Model().to('cuda')



A1 = torch.randn(4, 4)



A2 = torch.randn(4, 4)



A3 = torch.randn(4, 4)



A4 = torch.randn(4, 4)



A5 = torch.randn(4, 4)



A6 = torch.randn(4, 4)



A7 = torch.randn(4, 4)


test_inputs = [A1, A2, A3, A4, A5, A6, A7]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmplo5q4f4w/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmplo5q4f4w', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmplo5q4f4w/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
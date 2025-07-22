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

    def forward(self, x1, x2, x3, x4, x5, x6, x7):
        t1 = (((x1 + x5) + x6) + x7)
        t2 = ((x2 + x3) + x4)
        t3 = torch.mm(t1, t1)
        x = torch.mm(t2, t3)
        return x




func = Model().to('cuda')



input1 = torch.randn(50, 50)



input2 = torch.randn(50, 50)



input3 = torch.randn(50, 50)



input4 = torch.randn(50, 50)



input5 = torch.randn(50, 50)



input6 = torch.randn(50, 50)



input7 = torch.randn(50, 50)


test_inputs = [input1, input2, input3, input4, input5, input6, input7]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp4rh3bpk0/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp4rh3bpk0', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp4rh3bpk0/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
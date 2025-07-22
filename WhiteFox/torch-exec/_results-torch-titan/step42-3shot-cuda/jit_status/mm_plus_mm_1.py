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

    def forward(self, input1, input2, input3, input4, x, w, y, z):
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input3, input4)
        t3 = (t1 + t2)
        t4 = torch.mm(input3, input4)
        return (((((t4 + t3) + x) + w) + y) + z)




func = Model().to('cuda')



input1 = torch.randn(3, 4)



input2 = torch.randn(4, 3)



input3 = torch.randn(3, 4)



input4 = torch.randn(4, 3)



x = torch.randn(1)



w = torch.randn(1)



y = torch.randn(1)



z = torch.randn(1)


test_inputs = [input1, input2, input3, input4, x, w, y, z]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp36y3vsol/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp36y3vsol', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp36y3vsol/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
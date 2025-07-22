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

    def forward(self, x1, x2, x3):
        h1 = ((torch.mm(x1, x2) + torch.mm(x1, x3)) + torch.mm(x2, x3))
        h2 = ((torch.mm(x1, x1) + torch.mm(x2, x1)) + torch.mm(x3, x1))
        h3 = ((torch.mm(x1, x1) + torch.mm(x2, x2)) + torch.mm(x3, x3))
        return ((h1 + h2) + h3)




func = Model().to('cuda')



x1 = torch.randn(50, 50)



x2 = torch.randn(50, 50)



x3 = torch.randn(50, 50)


test_inputs = [x1, x2, x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpe7uuforv/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpe7uuforv', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpe7uuforv/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
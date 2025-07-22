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

    def _init_(self):
        super().__init__()

    def forward(self, X0, X1):
        v6 = (X0 * 0.25)
        v5 = (X0 * 0.3673)
        v7 = (v6 + X1)
        v8 = (v5 - X1)
        return (v7, v8)




func = Model().to('cuda')



x1 = torch.randn(16, 28, 4, 10)



x2 = torch.randn(1, 10)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpb5n3yz6_/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpb5n3yz6_', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpb5n3yz6_/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
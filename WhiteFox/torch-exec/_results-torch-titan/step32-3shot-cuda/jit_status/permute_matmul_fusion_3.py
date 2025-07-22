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
        v0 = x2.permute(0, 2, 1)
        v1 = torch.matmul(v0, x1)
        v2 = torch.matmul(v0, v1)
        v3 = v2.permute(0, 2, 1)
        v4 = torch.matmul(v0, v1)
        v5 = torch.matmul(x1, v3)
        v6 = torch.cat((v5, v4), 1)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)



x2 = torch.randn(1, 2, 2)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpgx8qm68e/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpgx8qm68e', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpgx8qm68e/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
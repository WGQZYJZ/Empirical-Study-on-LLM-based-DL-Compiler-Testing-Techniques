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

    def forward(self, x0, x1):
        v0 = x1.permute(0, 2, 1)
        v0 = x0.permute(0, 2, 1)
        v0 = x1.permute(0, 2, 1)
        v1 = x0.permute(0, 2, 1)
        v2 = torch.bmm(v0, v0)
        v3 = torch.bmm(v1, v1)
        return torch.tanh(v2)




func = Model().to('cuda')



x0 = torch.randn(1, 2, 2)



x1 = torch.randn(1, 2, 2)


test_inputs = [x0, x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp695uqkh1/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp695uqkh1', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp695uqkh1/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
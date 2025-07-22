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
        self.bn = torch.nn.BatchNorm1d(3, affine=False)
        self.linear = torch.nn.Linear(3, 3, False)

    def forward(self, x, inp):
        x1 = self.bn(x)
        v1 = self.linear(x1)
        v2 = (v1 + x1)
        v3 = torch.mm(v2, v2)
        return (v1, (v3 + inp), (v1.detach() + x))




func = Model().to('cuda')



x = torch.randn(3, 3)



inp = torch.randn(3, 3)


test_inputs = [x, inp]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp6v14tsek/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp6v14tsek', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp6v14tsek/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
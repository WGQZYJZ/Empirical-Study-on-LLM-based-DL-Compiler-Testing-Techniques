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
        self.conv = torch.nn.Conv2d(5, 7, 1, stride=1, padding=1)

    def forward(self, x1, other, padding1=None, conv=None):
        v1 = self.conv(x1)
        if (conv == None):
            conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        v2 = (v1 + other)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 5, 32, 32)



other = torch.randn(10)


test_inputs = [x1, other]

# JIT_FAIL
'''
direct:
The size of tensor a (34) must match the size of tensor b (10) at non-singleton dimension 3

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpmeo9qcd0/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpmeo9qcd0', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpmeo9qcd0/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
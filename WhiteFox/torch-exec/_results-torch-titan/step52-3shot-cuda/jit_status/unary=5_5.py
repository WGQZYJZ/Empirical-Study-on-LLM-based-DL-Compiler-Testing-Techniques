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
        self.conv_transpose = torch.nn.ConvTranspose2d(30, 10, 9, stride=9, padding=0)

    def forward(self, x0):
        v0 = self.conv_transpose(x0)
        v1 = (v0 * 0.5)
        v2 = (v0 * 0.7071067811865476)
        v3 = torch.erf(v2)
        v4 = (v3 + 1)
        v5 = (v1 * v4)
        return v5




func = Model().to('cuda')



x0 = torch.randn(1, 30, 32, 32)


test_inputs = [x0]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpnplwyuol/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpnplwyuol', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpnplwyuol/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
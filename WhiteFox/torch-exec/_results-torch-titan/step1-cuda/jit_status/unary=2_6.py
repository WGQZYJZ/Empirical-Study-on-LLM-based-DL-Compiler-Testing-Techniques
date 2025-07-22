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
        self.conv = torch.nn.ConvTranspose2d(3, 8, 3, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 * 0.5)
        v3 = (v1 + 0.5)
        v4 = (v1 * v2)
        v5 = (v4 * v2)
        v6 = (v3 * 0.044715)
        v7 = (v3 + v6)
        v8 = torch.tanh(v7)
        v9 = (v2 * 0.7978845608028654)
        v10 = (v2 + v9)
        v11 = (v1 * v10)
        v12 = (v11 * v10)
        return v12



func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpezyqixdo/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpezyqixdo', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpezyqixdo/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def forward(self, x1):
        v1 = (x1 * 0.5)
        v2 = (v1 * v1)
        v3 = (v2 * v1)
        v4 = (v3 * 0.044715)
        v5 = (x1 + v4)
        v6 = (v5 * 0.7978845608028654)
        v7 = torch.tanh(v6)
        v8 = (v7 + 1)
        v9 = (v8 * 0.5)
        v10 = (v8 * v8)
        v11 = (v10 * v8)
        v12 = (v11 * 0.044715)
        v13 = (v8 + v12)
        v14 = (v13 * 0.7978845608028654)
        v15 = torch.tanh(v14)
        v16 = (v15 + 1)
        v17 = (v9 * v16)
        return v17




func = Model().to('cuda')



x1 = torch.randn(1, 64, 16, 16)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpcitnhz1r/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpcitnhz1r', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpcitnhz1r/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
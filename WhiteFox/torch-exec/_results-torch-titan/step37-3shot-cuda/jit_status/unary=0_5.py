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
        self.conv1 = torch.nn.Conv2d(18, 36, 8, stride=2, padding=10)
        self.conv2 = torch.nn.Conv2d(36, 18, 9, stride=1, padding=1)

    def forward(self, x10):
        v1 = self.conv1(x10)
        v2 = (v1 * 0.5)
        v3 = (v1 * v1)
        v4 = (v3 * v1)
        v5 = (v4 * 0.044715)
        v6 = (v1 + v5)
        v7 = (v6 * 0.7978845608028654)
        v8 = torch.tanh(v7)
        v9 = (v8 + 1)
        v10 = (v2 * v9)
        v11 = self.conv2(v10)
        v12 = (v11 * 0.5)
        v13 = (v11 * v11)
        v14 = (v13 * v11)
        v15 = (v14 * 0.044715)
        v16 = (v11 + v15)
        v17 = (v16 * 0.7978845608028654)
        v18 = torch.tanh(v17)
        v19 = (v18 + 1)
        v20 = (v12 * v19)
        return v20




func = Model().to('cuda')



x10 = torch.randn(1, 18, 64, 64)


test_inputs = [x10]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpg9bxsefr/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpg9bxsefr', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpg9bxsefr/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
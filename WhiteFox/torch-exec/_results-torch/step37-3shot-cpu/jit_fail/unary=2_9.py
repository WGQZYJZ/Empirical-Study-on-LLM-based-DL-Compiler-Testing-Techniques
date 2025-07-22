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
        self.conv_transpose2d_0 = torch.nn.ConvTranspose2d(1, 9, (3, 3), stride=(2, 2))
        self.conv_transpose2d_1 = torch.nn.ConvTranspose2d(68, 31, (2, 2), stride=(1, 2), padding=(0, 2))

    def forward(self, x1):
        v1 = self.conv_transpose2d_0(x1)
        v2 = v1 * 0.5
        v3 = v1 * v1 * v1
        v4 = v3 * 0.044715
        v5 = v1 + v4
        v6 = v5 * 0.7978845608028654
        v7 = torch.tanh(v6)
        v8 = v7 + 1
        v9 = v2 * v8
        v10 = v9.contiguous()
        v11 = torch.tensor(0.13627589)
        v12 = torch.tensor(0.13627589)
        v13 = torch.add(v12, x1)
        v14 = torch.mul(v13, v11)
        v15 = v14.size(0)
        v16 = torch.tensor(0)
        v17 = torch.tensor(1)
        v18 = torch.max(v16, v17)
        v19 = v15 + v18
        v20 = torch.tensor(0)
        v21 = torch.tensor(1)
        v22 = torch.max(v20, v21)
        v23 = torch.floor((v19 + v22) / 4)
        v24 = v10.view(v23, 4, 17, 9)
        v25 = self.conv_transpose2d_1(v24)
        return v25



func = Model().to('cpu')


x1 = torch.randn(55, 1, 18, 21)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
view() received an invalid combination of arguments - got (Tensor, int, int, int), but expected one of:
 * (torch.dtype dtype)
 * (tuple of ints size)


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpklxfgyyj/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpklxfgyyj/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpklxfgyyj', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
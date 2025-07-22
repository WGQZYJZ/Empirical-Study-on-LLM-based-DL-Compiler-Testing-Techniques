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

    def forward(self, x1, x2, x3, x4):
        v1 = x1 * 0.5
        v2 = x1 * x1
        v3 = v2 * x1
        v4 = v3 * 0.044715
        v5 = x1 + v4
        v6 = v5 * 0.7978845608028654
        v7 = torch.tanh(v6)
        v8 = v7 + 1
        v9 = v1 * v8
        v10 = x2 * 0.5
        v11 = x2 * x2
        v12 = v11 * x2
        v13 = v12 * 0.044715
        v14 = x2 + v13
        v15 = v14 * 0.7978845608028654
        v16 = torch.tanh(v15)
        v17 = v16 + 1
        v18 = v10 * v17
        v19 = x3 * 0.5
        v20 = x3 * x3
        v21 = v20 * x3
        v22 = v21 * 0.044715
        v23 = x3 + v22
        v24 = v23 * 0.7978845608028654
        v25 = torch.tanh(v24)
        v26 = v25 + 1
        v27 = v19 * v26
        v28 = x4 * 0.5
        v29 = x4 * x4
        v30 = v29 * x4
        v31 = v30 * 0.044715
        v32 = x4 + v31
        v33 = v32 * 0.7978845608028654
        v34 = torch.tanh(v33)
        v35 = v34 + 1
        v36 = v28 * v35
        v37 = v9 + v18 + v27 + v36
        v38 = v37 * 0.7978845608028654
        v39 = torch.tanh(v38)
        v40 = v39 + 1
        return v40



func = Model().to('cpu')


x1 = torch.randn(1, 128, 100, 120)

x2 = torch.randn(1, 128, 100, 120)

x3 = torch.randn(1, 128, 100, 120)

x4 = torch.randn(1, 128, 100, 120)

test_inputs = [x1, x2, x3, x4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp2utzpi3m/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp2utzpi3m/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp2utzpi3m', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
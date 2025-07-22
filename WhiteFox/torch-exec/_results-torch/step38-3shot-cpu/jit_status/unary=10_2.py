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
        self.l1 = torch.nn.Linear(16, 8)
        self.l2 = torch.nn.Linear(8, 7)
        self.l3 = torch.nn.Linear(7, 6)
        self.l4 = torch.nn.Linear(6, 5)
        self.l5 = torch.nn.Linear(5, 4)

    def forward(self, x1):
        v1 = self.l1(x1)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        v6 = self.l2(v5)
        v7 = v6 + 5
        v8 = torch.clamp_min(v7, 0)
        v9 = torch.clamp_max(v8, 6)
        v10 = v9 / 6
        v11 = self.l3(v10)
        v12 = v11 + 9
        v13 = torch.clamp_min(v12, 0)
        v14 = torch.clamp_max(v13, 6)
        v15 = v14 / 6
        v16 = self.l4(v15)
        v17 = v16 + 7
        v18 = torch.clamp_min(v17, 0)
        v19 = torch.clamp_max(v18, 6)
        v20 = v19 / 6
        v21 = self.l5(v20)
        v22 = v21 + 6
        v23 = torch.clamp_min(v22, 0)
        v24 = torch.clamp_max(v23, 6)
        v25 = v24 / 6
        return v25


func = Model().to('cpu')


x1 = torch.randn(1, 16)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpuydluy02/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpuydluy02/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpuydluy02', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
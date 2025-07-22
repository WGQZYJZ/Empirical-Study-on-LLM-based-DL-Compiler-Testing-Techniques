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

    def __init__(self, in_features: int, out_features: int):
        super().__init__()
        self.matmul1 = torch.nn.Linear(in_features, 64)
        in_features_for_matmul2 = in_features + 64
        self.matmul2 = torch.nn.Linear(in_features_for_matmul2, out_features)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v1 = self.matmul1(x1)
        v2 = self.relu(v1)
        v3 = torch.cat([x1, v2], -1)
        v4 = self.matmul2(v3)
        return v4


in_features = 1
out_features = 1
func = Model(3, 3).to('cuda')


x1 = torch.randn(1, 3)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpdwzmrxqx/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpdwzmrxqx/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpdwzmrxqx', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
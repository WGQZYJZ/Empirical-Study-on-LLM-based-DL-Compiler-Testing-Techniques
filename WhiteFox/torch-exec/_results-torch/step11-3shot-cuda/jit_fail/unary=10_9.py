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
        self.linear = torch.nn.Linear(4, 3)

    def forward(self, x1):
        v0 = torch.nn.functional.gelu(x1)
        v1 = torch.nn.functional.gelu(x1, False)
        v2 = torch.nn.functional.gelu(x1, True)
        l1 = self.linear(x1)
        l2 = l1 + 3
        l3 = torch.clamp_min(l2, 0)
        l4 = torch.clamp_max(l3, 6)
        l5 = l4 / 6
        v3 = torch.nn.functional.leaky_relu(x1)
        v4 = torch.nn.functional.leaky_relu(x1, 0.3933874983975471)
        v5 = torch.nn.functional.leaky_relu(x1, 0.3933874983975471, True)
        v6 = torch.nn.functional.relu(x1)
        v7 = torch.nn.functional.relu(x1, True)
        v8 = torch.nn.functional.mish(x1)
        v9 = torch.nn.functional.hardsigmoid(x1)
        v10 = torch.nn.functional.hardsigmoid(x1, True)
        v11 = torch.nn.functional.hardswish(x1)
        return (v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11)


func = Model().to('cuda')


x1 = torch.randn(1, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
gelu() takes 1 positional argument but 2 were given

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp9_hzk9vj/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp9_hzk9vj/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp9_hzk9vj', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
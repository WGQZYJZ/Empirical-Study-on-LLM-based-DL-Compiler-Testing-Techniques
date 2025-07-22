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
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.transpose(0, 1)
        v2 = torch.nn.functional.linear(v1, self.linear1.weight, self.linear1.bias)
        x2 = torch.nn.functional.linear(v2, self.linear2.weight, self.linear2.bias)
        x3 = torch.nn.functional.sigmoid(x2)
        v3 = x3.detach()
        v4 = torch.max(v3, dim=1)[1]
        v5 = x1.detach()
        v5 = v5.transpose(0, 1)
        v5 = 2 * v5
        v5 = v5[v4]
        v3 = x3 + v5.to(dtype=x3.dtype)
        return torch.nn.functional.relu(v3)



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpwekjxmbo/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpwekjxmbo/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpwekjxmbo', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
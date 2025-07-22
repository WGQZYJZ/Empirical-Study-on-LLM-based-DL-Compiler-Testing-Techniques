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

class MyModel(torch.nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.tanh(x1)
        v1 = torch.max_pool2d(v0, 2)
        v2 = torch.conv_transpose2d(v1, 4, 6, (4, 4))
        v3 = torch.max_pool2d(v2, 2)
        v4 = torch.conv2d(v3, 1, (3, 3))
        v5 = torch.tanh(v4)
        return v5



func = MyModel().to('cpu')


x1 = torch.randn(1, 4, 6, 6)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv_transpose2d(): argument 'weight' (position 2) must be Tensor, not int

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpyn0dj6cg/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpyn0dj6cg/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpyn0dj6cg', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        x2 = torch.cat([x1, x1, x1, x1], 1)
        conv1 = torch.nn.Conv2d(4, 4, 1)
        x2 = conv1(x2)
        bn_module = torch.nn.BatchNorm2d(4)
        bn_module.running_mean = torch.ones_like(bn_module.bias, dtype=torch.float32)
        bn_module.running_var = torch.ones_like(bn_module.bias, dtype=torch.float32)
        x2 = bn_module(x2)
        conv2 = torch.nn.Conv2d(4, 1, 1)
        x2 = conv2(x2)
        return x2



func = Model().to('cuda')


x1 = torch.randn(1, 3, 4, 4)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given groups=1, weight of size [4, 4, 1, 1], expected input[1, 12, 4, 4] to have 4 channels, but got 12 channels instead

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp39vgtwyb/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp39vgtwyb/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp39vgtwyb', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def __init__(self, stride, padding):
        super().__init__()
        self.conv1a = torch.nn.Conv2d(3, 8, 7, stride=stride, padding=padding)
        self.conv1b = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0)

    def forward(self, x):
        x = self.conv1a(x)
        x = torch.clamp_min(x, 0.4226538)
        x = torch.clamp_max(x, 0.38730868)
        x = self.conv1b(x)
        x = torch.clamp_min(x, 0.85527596)
        x = torch.clamp_max(x, 0.45974174)
        return x


stride = 1
padding = 0

func = Model(stride, padding).to('cpu')


x = torch.randn(1, 3, 400, 398)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp4gdh78jq/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp4gdh78jq/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp4gdh78jq', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
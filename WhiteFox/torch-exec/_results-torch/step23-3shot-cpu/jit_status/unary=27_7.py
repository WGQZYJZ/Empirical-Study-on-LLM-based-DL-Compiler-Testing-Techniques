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

    def __init__(self, min_r, max_r, min_g, max_g, min_b, max_b):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 1, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(1, 1, 1, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(1, 1, 1, stride=4, padding=0)
        self.conv4 = torch.nn.Conv2d(1, 1, 1, stride=2, padding=2)
        self.min_r = min_r
        self.max_r = max_r
        self.min_g = min_g
        self.max_g = max_g
        self.min_b = min_b
        self.max_b = max_b

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.clamp(v1, min=self.min_r, max=self.max_r)
        v3 = torch.clamp(v2, min=self.min_g, max=self.max_g)
        v4 = torch.clamp(v3, min=self.min_b, max=self.max_b)
        v5 = torch.clamp(v4, min=-0.4182, max=0.8147)
        v6 = self.conv2(v5)
        v7 = self.conv3(v6)
        v8 = self.conv4(v7)
        return v8


min_r = -2.9786
max_r = 0.6274
min_g = -0.1683
max_g = 3.0743
min_b = 0.197
max_b = -0.5785

func = Model(min_r, max_r, min_g, max_g, min_b, max_b).to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpl88jd62b/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpl88jd62b/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpl88jd62b', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
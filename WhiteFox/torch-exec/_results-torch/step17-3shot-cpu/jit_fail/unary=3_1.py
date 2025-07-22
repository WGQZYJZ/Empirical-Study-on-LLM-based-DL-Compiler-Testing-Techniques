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
        self.conv1 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=0, dilation=2)
        self.conv2 = torch.nn.Conv2d(32, 32, 1, stride=1, padding=0, dilation=2)
        self.conv3 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=2, dilation=2)
        self.conv4 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=2, dilation=2)
        self.conv5 = torch.nn.Conv2d(32, 32, 3, stride=1, padding=1, dilation=2)
        self.conv6 = torch.nn.Conv2d(32, 32, 1, stride=1, padding=0, dilation=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        b1 = nn.BatchNorm2d(32)
        v2 = b1(v1)
        v3 = v2 * 0.5
        v4 = v2 * 0.7071067811865476
        v5 = torch.erf(v4)
        v6 = v5 + 1
        v7 = v3 * v6
        v8 = self.conv2(v1)
        v9 = self.conv3(v1)
        v10 = self.conv4(v1)
        v11 = self.conv5(v1)
        v12 = self.conv6(v3)
        v13 = v11 * 0.5
        v14 = v11 * 0.7071067811865476
        v15 = torch.erf(v14)
        v16 = v15 + 1
        v17 = v13 * v16
        v18 = (v7 - v17) * v12
        v19 = v8 * v18
        v20 = b1(v3)
        v21 = b1(v8)
        v22 = b1(v9)
        v23 = b1(v10)
        return v19



func = Model().to('cpu')


x1 = torch.randn(1, 32, 90, 90)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (86) must match the size of tensor b (84) at non-singleton dimension 3

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp0gxcr6dv/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp0gxcr6dv/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp0gxcr6dv', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
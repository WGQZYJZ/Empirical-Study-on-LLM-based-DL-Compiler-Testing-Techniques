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
        self.conv = torch.nn.Conv2d(2, 85, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(85, 35, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(35, 70, 3, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(70, 33, 1, stride=1, padding=0)
        self.conv5 = torch.nn.Conv2d(33, 67, 3, stride=1, padding=1)
        self.conv6 = torch.nn.Conv2d(67, 58, 1, stride=1, padding=0)
        self.conv7 = torch.nn.Conv2d(58, 34, 3, stride=1, padding=1)
        self.conv8 = torch.nn.Conv2d(34, 45, 1, stride=1, padding=0)
        self.conv9 = torch.nn.Conv2d(45, 87, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.conv2(v6)
        v8 = self.conv3(v7)
        v9 = v8 * 0.5
        v10 = v8 * 0.7071067811865476
        v11 = torch.erf(v10)
        v12 = v11 + 1
        v13 = v9 * v12
        v14 = self.conv4(v13)
        v15 = self.conv5(v14)
        v16 = v15 * 0.5
        v17 = v15 * 0.7071067811865476
        v18 = torch.erf(v17)
        v19 = v18 + 1
        v20 = v16 * v19
        v21 = self.conv6(v20)
        v22 = self.conv7(v21)
        v23 = v22 * 0.5
        v24 = v22 * 0.7071067811865476
        v25 = torch.erf(v24)
        v26 = v25 + 1
        v27 = v23 * v26
        v28 = self.conv8(v27)
        v29 = self.conv9(v28)
        return v29



func = Model().to('cuda')


x1 = torch.randn(1, 2, 7, 9)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp1nue5ufb/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp1nue5ufb/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp1nue5ufb', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
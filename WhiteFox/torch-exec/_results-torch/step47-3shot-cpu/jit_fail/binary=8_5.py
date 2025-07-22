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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(8)
        self.bn2 = torch.nn.BatchNorm2d(8)

    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(x2)
        v3 = v1 + v2
        v4 = self.bn1(v1)
        v5 = self.bn2(v2)
        v6 = torch.sin(v3 + v4 + v5)
        v7 = torch.cos(v3 + v4 + v5)
        v8 = torch.relu(v3 + v4 + v5)
        v9 = v6.mul(v7).div(v8).pow(v3 + v4 - v5)
        v10 = torch.abs(v3 + v4 + v5)
        v11 = v9.div(v10).mul(v4 + v5)
        v12 = torch.clamp(v4 + v5, max=3, min=1).mul(v11)
        v13 = torch.ceil(v12 + 0.5 + v5).sub(0.4 + v5).clamp(-1.0 + v2, 2)
        v14 = v13.reciprocal().clamp(min=1, max=2)
        v15 = v13.neg().addcmul(0.5, v14, value=0.22 + v5).sign()
        v16 = v15.sub(v13.mul(v12)).div(v15.add(v12)).tanh().add(1 + v2)
        v17 = v11.sub(0.4 + v5).div(v6).mul(v3.pow(0.5 + v16) - v7).floor()
        return v17.neg().sub(1 + v18)



func = Model().to('cpu')


x1 = torch.randn(1, 3, 32, 32)

x2 = torch.randn(1, 3, 32, 32)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
clamp() received an invalid combination of arguments - got (Tensor, int), but expected one of:
 * (Tensor min = None, Tensor max = None)
      didn't match because some of the arguments have invalid types: (!Tensor!, !int!)
 * (Number min = None, Number max = None)
      didn't match because some of the arguments have invalid types: (!Tensor!, !int!)


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpx4j7o_sn/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpx4j7o_sn/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpx4j7o_sn', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
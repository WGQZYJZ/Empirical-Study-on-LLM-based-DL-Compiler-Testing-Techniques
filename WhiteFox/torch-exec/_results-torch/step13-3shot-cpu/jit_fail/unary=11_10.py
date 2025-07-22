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
        self.relu6 = torch.nn.ReLU6()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 10, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.relu6(x1)
        v2 = self.relu6(v1)
        v3 = self.relu6(v2)
        v4 = self.conv_transpose(v1)
        v5 = v4 + 3
        v6 = self.relu6(v5)
        v7 = self.relu6(v6)
        v8 = self.relu6(v7)
        v9 = self.conv_transpose(v2)
        v10 = v9 + 3
        v11 = self.relu6(v10)
        v12 = self.relu6(v11)
        v13 = self.relu6(v12)
        v14 = torch.min(v8, v13)
        v15 = torch.max(v14, v15)
        v16 = v15 / 6
        return v16



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
local variable 'v15' referenced before assignment

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpjqg0bno8/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpjqg0bno8/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpjqg0bno8', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
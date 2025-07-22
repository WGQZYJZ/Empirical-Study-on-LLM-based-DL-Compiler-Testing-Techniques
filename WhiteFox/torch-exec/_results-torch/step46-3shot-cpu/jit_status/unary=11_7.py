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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(3, 32, 3, stride=2, padding=1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(32, 64, 3, stride=2, padding=1)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(64, 64, 3, stride=2, padding=1)
        self.conv_transpose4 = torch.nn.ConvTranspose2d(64, 64, 3, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1) + 3
        v2 = torch.clamp_min(v1, 0)
        v3 = torch.clamp_max(v2, 6)
        v4 = v3 / 6
        v5 = self.conv_transpose2(v4) + 3
        v6 = torch.clamp_min(v5, 0)
        v7 = torch.clamp_max(v6, 6)
        v8 = v7 / 6
        v9 = self.conv_transpose3(v8) + 3
        v10 = torch.clamp_min(v9, 0)
        v11 = torch.clamp_max(v10, 6)
        v12 = v11 / 6
        v13 = self.conv_transpose4(v12) + 3
        v14 = torch.clamp_min(v13, 0)
        v15 = torch.clamp_max(v14, 6)
        v16 = v15 / 6
        return v16



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpg0octipv/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpg0octipv/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpg0octipv', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
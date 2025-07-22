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
        self.conv06 = torch.nn.Conv2d(1, 1, kernel_size=(6, 1), stride=(6, 1), padding=(4, 0))
        self.conv01 = torch.nn.Conv2d(1, 1, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0))

    def forward(self, x1):
        x1 = self.conv06(x1)
        x1 = x1 + 0.3
        x1 = self.conv01(x1)
        x1 = x1.add(2.5)
        x1 = self.conv06(x1)
        x1 = x1 + 0.3
        x1 = self.conv01(x1)
        x1 = x1.add(2.5)
        return x1.clamp(min=0.0, max=6.0) / 6.0



func = Model().to('cpu')


x1 = torch.randn(1, 1, 64, 1)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpphgmiiot/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpphgmiiot/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpphgmiiot', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
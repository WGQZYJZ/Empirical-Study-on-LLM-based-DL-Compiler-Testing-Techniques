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
        self.conv = torch.nn.Conv2d(10, 10, 3)

    def forward(self, x):
        x = self.conv(x)
        x = torch.cat([x, x, x], dim=1)
        x = torch.dropout(x)
        x = torch.relu(-3.0 * x)
        x = torch.sigmoid(1.0 + x) if x.shape[1] == 1 else torch.sigmoid(1.0 - x)
        x = torch.sin(x)
        return x



func = Model().to('cpu')


x = torch.randn(1, 10, 3, 11)

test_inputs = [x]

# JIT_FAIL
'''
direct:
dropout() missing 2 required positional argument: "p", "train"

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpphr1losx/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpphr1losx/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpphr1losx', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
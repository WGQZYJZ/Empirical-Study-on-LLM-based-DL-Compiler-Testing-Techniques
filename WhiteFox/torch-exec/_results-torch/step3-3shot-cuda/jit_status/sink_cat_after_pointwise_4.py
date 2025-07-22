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
        self.conv = nn.Conv2d(16, 16, kernel_size=3, stride=1, padding=1, bias=False)

    def forward(self, input):
        x = self.conv(input)
        x = x.mean([2, 3])
        x = x.unsqueeze(2)
        x = x.view(x.shape[0], x.shape[1], x.shape[2], 1, 1)
        x = x.repeat(1, 1, 1, 3, 3)
        x = x * x
        x = x.reshape(x.shape[0], x.shape[1], -1)
        x = x * x
        return x



func = Model().to('cuda')


input = torch.randn(1, 16, 64, 64)

test_inputs = [input]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpgoaa7wha/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpgoaa7wha/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpgoaa7wha', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
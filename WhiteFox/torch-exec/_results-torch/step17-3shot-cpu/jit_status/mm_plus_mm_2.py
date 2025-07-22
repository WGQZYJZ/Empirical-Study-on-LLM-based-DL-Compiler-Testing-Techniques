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
        self.conv_block = torch.nn.Sequential(torch.nn.Conv2d(3, 16, kernel_size=(3, 3), stride=1), torch.nn.Conv2d(16, 16, kernel_size=(1, 1), stride=1), torch.nn.Conv2d(16, 16, kernel_size=(3, 3), stride=1), torch.nn.Conv2d(16, 16, kernel_size=(3, 3), stride=1), torch.nn.Conv2d(16, 16, kernel_size=(3, 3), stride=1))

    def forward(self, x):
        x = self.conv_block(x)
        return x


func = Model().to('cpu')


input_shape = (2, 3, 224, 224)
x = torch.randn(input_shape)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpcs2s3ydq/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpcs2s3ydq/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpcs2s3ydq', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

class Model_2(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv3d = torch.nn.Conv3d(3, 3, kernel_size=3, padding=[2, 1, 1], bias=True)
        self.relu = torch.nn.ReLU(inplace=True)
        self.maxpool3d = torch.nn.MaxPool3d(kernel_size=2, padding=0, stride=1, dilation=1, ceil_mode=False)
        self.sigmoid = torch.nn.Sigmoid()
        self.dropout = torch.nn.Dropout3d(p=0)

    def forward(self, x1):
        v1 = self.conv3d(x1)
        v2 = self.relu(v1)
        v3 = torch.max(v2, dim=2, keepdim=True)
        v4 = torch.mean(v3, dim=2, keepdim=True)
        v5 = self.sigmoid(v4)
        v6 = self.dropout(v5)
        return v6



func = Model_2().to('cpu')


x1 = torch.randn(1, 3, 64, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mean() received an invalid combination of arguments - got (torch.return_types.max, keepdim=bool, dim=int), but expected one of:
 * (Tensor input, *, torch.dtype dtype = None, Tensor out = None)
 * (Tensor input, tuple of ints dim, bool keepdim = False, *, torch.dtype dtype = None, Tensor out = None)
 * (Tensor input, tuple of names dim, bool keepdim = False, *, torch.dtype dtype = None, Tensor out = None)


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp69i4lmvv/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp69i4lmvv/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp69i4lmvv', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
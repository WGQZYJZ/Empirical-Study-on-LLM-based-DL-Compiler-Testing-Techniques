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
        self.conv_transpose_0 = torch.nn.ConvTranspose3d(20, 50, 1, stride=1, padding=0)
        self.conv_transpose_1 = torch.nn.ConvTranspose3d(50, 10, 2, stride=3, padding=1)
        self.conv_transpose_2 = torch.nn.ConvTranspose3d(10, 5, 4, stride=4, padding=2)

    def forward(self, x1):
        v1 = self.conv_transpose_0(x1)
        v2 = torch.sigmoid(v1)
        v3 = (v1 * v2)
        v4 = self.conv_transpose_1(v3)
        v5 = torch.sigmoid(v4)
        v6 = (v4 * v5)
        v7 = self.conv_transpose_2(v6)
        v8 = torch.sigmoid(v7)
        v9 = (v7 * v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 20, 120, 104, 20)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
CUDA out of memory. Tried to allocate 7.32 GiB. GPU 0 has a total capacty of 23.69 GiB of which 6.88 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 16.55 GiB memory in use. Of the allocated memory 16.08 GiB is allocated by PyTorch, and 171.74 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp7po9ijyk/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp7po9ijyk', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp7po9ijyk/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
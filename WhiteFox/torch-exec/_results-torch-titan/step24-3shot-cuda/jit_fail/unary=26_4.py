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

    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, 3, stride=1, padding=1)
        self.conv_t = torch.nn.ConvTranspose2d(1, 250, 95, stride=145)
        self.negative_slope = negative_slope

    def forward(self, x4):
        v1 = self.conv(x4)
        v2 = self.conv_t(v1)
        v3 = (v2 > 0)
        v4 = (v2 * self.negative_slope)
        v5 = torch.where(v3, v2, v4)
        return v5




negative_slope = 1.386


func = Model(negative_slope).to('cuda')



x4 = torch.randn(3, 1, 23, 122)


test_inputs = [x4]

# JIT_FAIL
'''
direct:
CUDA out of memory. Tried to allocate 161.90 GiB. GPU 0 has a total capacty of 23.69 GiB of which 22.97 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 462.00 MiB memory in use. Of the allocated memory 40.94 MiB is allocated by PyTorch, and 109.06 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpn9kzug6r/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpn9kzug6r', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpn9kzug6r/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
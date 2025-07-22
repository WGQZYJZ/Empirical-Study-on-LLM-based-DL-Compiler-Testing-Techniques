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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 256, kernel_size=1)
        self.conv_1 = torch.nn.Conv2d(256, 1024, 1)
        self.conv_2 = torch.nn.Conv2d(1024, 5, 1)
        self.sig = torch.nn.Sigmoid()

    def forward(self, x):
        v1 = self.conv_1(self.conv(x))
        v2 = torch.tanh(v1)
        self.conv_2(v2)
        v3 = torch.tanh(v2)
        v4 = self.sig(self.conv_2(v3)).squeeze(1)
        return v4




func = ModelTanh().to('cuda')



x = torch.randn(128, 16, 256, 256)


test_inputs = [x]

# JIT_FAIL
'''
direct:
CUDA out of memory. Tried to allocate 32.00 GiB. GPU 0 has a total capacty of 23.69 GiB of which 14.12 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 9.30 GiB memory in use. Of the allocated memory 9.00 GiB is allocated by PyTorch, and 982.50 KiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp01kuzg5n/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp01kuzg5n', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp01kuzg5n/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
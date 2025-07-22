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
        self.layer_0 = torch.nn.ConvTranspose2d(8, 8, 3, stride=17, padding=1, bias=False)
        self.layer_1 = torch.nn.ConvTranspose2d(8, 8, 3, stride=17, padding=1)

    def forward(self, x1):
        v1 = self.layer_0(x1)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        v7 = self.layer_1(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 8, 128, 128)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
CUDA out of memory. Tried to allocate 40.15 GiB. GPU 0 has a total capacty of 23.69 GiB of which 22.27 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 1.15 GiB memory in use. Of the allocated memory 855.34 MiB is allocated by PyTorch, and 12.66 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_5al5_p3/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp_5al5_p3', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp_5al5_p3/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv_t = torch.nn.ConvTranspose2d(44, 27, 3, stride=2, padding=0, bias=False)
        self.conv_t_0 = torch.nn.ConvTranspose2d(27, 39, 3, stride=2, padding=0, bias=False)
        self.conv_t_1 = torch.nn.ConvTranspose2d(39, 57, 3, stride=2, padding=0, bias=False)
        self.conv_t_2 = torch.nn.ConvTranspose2d(57, 94, 3, stride=2, padding=0, bias=False)

    def forward(self, x4):
        y0 = torch.nn.Softplus()(self.conv_t(x4))
        y1 = torch.nn.Softplus()(self.conv_t_0(y0))
        y2 = torch.nn.Softplus()(self.conv_t_1(y1))
        return torch.nn.Softplus()(self.conv_t_2(y2))




func = Model().to('cuda')



x4 = torch.randn(7, 44, 399, 745)


test_inputs = [x4]

# JIT_FAIL
'''
direct:
CUDA out of memory. Tried to allocate 28.37 GiB. GPU 0 has a total capacty of 23.69 GiB of which 15.19 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 8.23 GiB memory in use. Of the allocated memory 6.38 GiB is allocated by PyTorch, and 1.55 GiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmprrrmcbc9/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmprrrmcbc9', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmprrrmcbc9/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
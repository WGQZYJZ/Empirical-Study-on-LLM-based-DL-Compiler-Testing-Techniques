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
        self.conv = torch.nn.ConvTranspose2d(6, 6, 1, padding=1, stride=2)
        self.conv1 = torch.nn.Conv2d(6, 32, 1, padding=0)
        self.conv2 = torch.nn.ConvTranspose2d(32, 32, 3, padding=1, stride=2)
        self.conv3 = torch.nn.Conv2d(32, 64, 1, padding=0)
        self.conv4 = torch.nn.Conv2d(64, 64, 3, padding=1)
        self.conv5 = torch.nn.Conv2d(64, 64, 1)

    def forward(self, x1):
        v6 = self.conv(x1)
        v7 = torch.sigmoid(v6)
        v8 = nn.functional.interpolate(v7, scale_factor=2, mode='nearest')
        v9 = self.conv1(v8)
        v10 = torch.sigmoid(v9)
        v11 = nn.functional.interpolate(v10, scale_factor=2, mode='nearest')
        v12 = self.conv2(v11)
        v13 = torch.sigmoid(v12)
        v14 = nn.functional.interpolate(v13, scale_factor=2, mode='nearest')
        v15 = self.conv3(v14)
        v16 = torch.sigmoid(v15)
        v17 = nn.functional.interpolate(v16, scale_factor=2, mode='nearest')
        v18 = self.conv4(v17)
        v19 = torch.sigmoid(v18)
        v20 = nn.functional.interpolate(v19, scale_factor=2, mode='nearest')
        v21 = self.conv5(v20)
        v22 = torch.sigmoid(v21)
        return v22




func = Model().to('cuda')



x1 = torch.randn(1, 6, 242, 242)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
CUDA out of memory. Tried to allocate 14.12 GiB. GPU 0 has a total capacty of 23.69 GiB of which 11.33 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 12.09 GiB memory in use. Of the allocated memory 11.28 GiB is allocated by PyTorch, and 518.71 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp1otzog3f/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp1otzog3f', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp1otzog3f/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
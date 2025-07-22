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
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(128, 96, 3, stride=2, padding=1)
        self.conv_transpose_4 = torch.nn.ConvTranspose2d(96, 64, 5, stride=2, padding=1, groups=2)
        self.conv_transpose_6 = torch.nn.ConvTranspose2d(64, 32, 3, stride=2, padding=1)
        self.conv_transpose_8 = torch.nn.ConvTranspose2d(32, 64, 3, stride=2, padding=1)
        self.conv_transpose_10 = torch.nn.ConvTranspose2d(64, 96, 3, stride=2, padding=1)
        self.conv_transpose_12 = torch.nn.ConvTranspose2d(96, 128, 3, stride=2, padding=1)
        self.conv_transpose_14 = torch.nn.ConvTranspose2d(128, 48, 3, stride=2, padding=1)
        self.conv_transpose_16 = torch.nn.ConvTranspose2d(48, 24, 7, stride=2, padding=3)
        self.conv_transpose_18 = torch.nn.ConvTranspose2d(24, 48, 3, stride=2, padding=1)
        self.conv_transpose_20 = torch.nn.ConvTranspose2d(48, 6, 3, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose_2(x1)
        v2 = torch.sigmoid(v1)
        v3 = (v1 * v2)
        v4 = self.conv_transpose_4(v3)
        v5 = torch.sigmoid(v4)
        v6 = (v4 * v5)
        v7 = self.conv_transpose_6(v6)
        v8 = torch.sigmoid(v7)
        v9 = (v7 * v8)
        v10 = self.conv_transpose_8(v9)
        v11 = torch.sigmoid(v10)
        v12 = (v10 * v11)
        v13 = self.conv_transpose_10(v12)
        v14 = torch.sigmoid(v13)
        v15 = (v13 * v14)
        v16 = self.conv_transpose_12(v15)
        v17 = torch.sigmoid(v16)
        v18 = (v16 * v17)
        v19 = self.conv_transpose_14(v18)
        v20 = torch.sigmoid(v19)
        v21 = (v19 * v20)
        v22 = self.conv_transpose_16(v21)
        v23 = torch.sigmoid(v22)
        v24 = (v22 * v23)
        v25 = self.conv_transpose_18(v24)
        v26 = torch.sigmoid(v25)
        v27 = (v25 * v26)
        v28 = self.conv_transpose_20(v27)
        v29 = torch.sigmoid(v28)
        v30 = (v28 * v29)
        return v30




func = Model().to('cuda')



x1 = torch.randn(1, 128, 12, 12)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
CUDA out of memory. Tried to allocate 6.20 GiB. GPU 0 has a total capacty of 23.69 GiB of which 4.67 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 18.76 GiB memory in use. Of the allocated memory 16.85 GiB is allocated by PyTorch, and 1.60 GiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpbr4dkixa/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpbr4dkixa', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpbr4dkixa/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
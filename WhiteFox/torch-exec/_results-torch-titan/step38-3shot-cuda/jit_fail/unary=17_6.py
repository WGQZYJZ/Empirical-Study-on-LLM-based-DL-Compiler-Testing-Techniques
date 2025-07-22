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
        self.conv = torch.nn.ConvTranspose2d(3, 1024, 7, stride=7, padding=0)
        self.conv1 = torch.nn.ConvTranspose2d(1024, 512, 21, stride=5, padding=0)
        self.conv2 = torch.nn.ConvTranspose2d(512, 256, 51, stride=15, padding=0)
        self.conv3 = torch.nn.ConvTranspose2d(256, 256, 101, stride=15, padding=0)
        self.conv4 = torch.nn.ConvTranspose2d(256, 128, 201, stride=7, padding=0)
        self.conv5 = torch.nn.ConvTranspose2d(128, 64, 56, stride=1, padding=0)
        self.conv6 = torch.nn.ConvTranspose2d(64, 32, 16, stride=4, padding=0)
        self.conv7 = torch.nn.ConvTranspose2d(32, 32, 5, stride=2, padding=0)
        self.conv8 = torch.nn.ConvTranspose2d(32, 16, 3, stride=2, padding=0)
        self.conv9 = torch.nn.ConvTranspose2d(16, 1, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        v3 = self.conv1(v2)
        v4 = torch.relu(v3)
        v5 = self.conv2(v4)
        v6 = torch.relu(v5)
        v7 = self.conv3(v6)
        v8 = torch.relu(v7)
        v9 = self.conv4(v8)
        v10 = torch.relu(v9)
        v11 = self.conv5(v10)
        v12 = torch.relu(v11)
        v13 = self.conv6(v12)
        v14 = torch.relu(v13)
        v15 = self.conv7(v14)
        v16 = self.conv8(v15)
        v17 = self.conv9(v16)
        return v17




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
CUDA out of memory. Tried to allocate 168.82 GiB. GPU 0 has a total capacty of 23.69 GiB of which 2.16 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 21.27 GiB memory in use. Of the allocated memory 20.90 GiB is allocated by PyTorch, and 69.15 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpb5raol3u/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpb5raol3u', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpb5raol3u/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
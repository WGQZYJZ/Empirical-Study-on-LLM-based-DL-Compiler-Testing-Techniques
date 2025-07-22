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
        self.conv_transpose_1 = torch.nn.ConvTranspose2d(160, 64, 2, stride=2, padding=(0, 0))
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(64, 128, 2, stride=2, padding=(1, 1))
        self.conv_transpose_3 = torch.nn.ConvTranspose2d(128, 16, 2, stride=2, padding=(0, 0))
        self.conv_transpose_4 = torch.nn.ConvTranspose2d(16, 8, 2, stride=2, padding=(1, 1))
        self.conv_transpose_5 = torch.nn.ConvTranspose2d(8, 8, 2, stride=2, padding=(0, 0))
        self.conv_transpose_6 = torch.nn.ConvTranspose2d(8, 8, 2, stride=2, padding=(1, 1))
        self.conv_transpose_7 = torch.nn.ConvTranspose2d(8, 64, 2, stride=2, padding=(0, 0))
        self.conv_transpose_8 = torch.nn.ConvTranspose2d(64, 512, 2, stride=2, padding=(1, 1))
        self.conv_transpose_9 = torch.nn.ConvTranspose2d(2048, 2, 2, stride=2, padding=(0, 1))

    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        v2 = torch.sigmoid(v1)
        v3 = (v1 * v2)
        v4 = self.conv_transpose_2(v3)
        v5 = torch.sigmoid(v4)
        v6 = (v4 * v5)
        v7 = self.conv_transpose_3(v6)
        v8 = torch.sigmoid(v7)
        v9 = (v7 * v8)
        v10 = self.conv_transpose_4(v9)
        v11 = torch.sigmoid(v10)
        v12 = (v10 * v11)
        v13 = self.conv_transpose_5(v12)
        v14 = torch.sigmoid(v13)
        v15 = (v13 * v14)
        v16 = self.conv_transpose_6(v15)
        v17 = torch.sigmoid(v16)
        v18 = (v16 * v17)
        v19 = self.conv_transpose_7(v18)
        v20 = torch.sigmoid(v19)
        v21 = (v19 * v20)
        v22 = self.conv_transpose_8(v21)
        v23 = torch.sigmoid(v22)
        v24 = (v22 * v23)
        v25 = self.conv_transpose_9(v24)
        return v25




func = Model().to('cuda')



x1 = torch.randn(1, 160, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
CUDA out of memory. Tried to allocate 122.74 GiB. GPU 0 has a total capacty of 23.69 GiB of which 10.92 GiB is free. Process 2006998 has 256.00 MiB memory in use. Including non-PyTorch memory, this process has 12.50 GiB memory in use. Of the allocated memory 12.03 GiB is allocated by PyTorch, and 176.04 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF

jit:
Failed running call_module L__self___conv_transpose_9(*(FakeTensor(..., device='cuda:0', size=(1, 512, 8022, 8022)),), **{}):
Given transposed=1, weight of size [2048, 2, 2, 2], expected input[1, 512, 8022, 8022] to have 2048 channels, but got 512 channels instead

from user code:
   File "<string>", line 54, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
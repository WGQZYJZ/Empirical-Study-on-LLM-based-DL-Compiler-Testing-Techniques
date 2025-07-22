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
        self.convTranspose = torch.nn.ConvTranspose2d(in_channels=16, out_channels=16, kernel_size=3, stride=4, padding=1)
        self.convTranspose2 = torch.nn.ConvTranspose2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.convTranspose3 = torch.nn.ConvTranspose2d(in_channels=32, out_channels=64, kernel_size=3, stride=4, padding=1)
        self.convTranspose4 = torch.nn.ConvTranspose2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1)
        self.convTranspose5 = torch.nn.ConvTranspose2d(in_channels=128, out_channels=64, kernel_size=3, stride=4, padding=1)
        self.convTranspose6 = torch.nn.ConvTranspose2d(in_channels=64, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.convTranspose7 = torch.nn.ConvTranspose2d(in_channels=32, out_channels=16, kernel_size=3, stride=4, padding=1)
        self.convTranspose8 = torch.nn.ConvTranspose2d(in_channels=16, out_channels=8, kernel_size=(10, 10), padding=2)

    def forward(self, x1):
        v1 = self.convTranspose(x1)
        v2 = torch.tanh(v1)
        v3 = self.convTranspose2(v2)
        v4 = torch.tanh(v3)
        v5 = self.convTranspose3(v4)
        v6 = torch.tanh(v5)
        v7 = self.convTranspose4(v6)
        v8 = torch.tanh(v7)
        v9 = self.convTranspose5(v8)
        v10 = torch.tanh(v9)
        v11 = self.convTranspose6(v10)
        v12 = torch.tanh(v11)
        v13 = self.convTranspose7(v12)
        v14 = torch.tanh(v13)
        v15 = self.convTranspose8(v14)
        v16 = torch.tanh(v15)
        v17 = torch.softmax(v16)
        v18 = torch.tanh(v17)
        v19 = torch.bmm(v18, v17)
        v20 = torch.tanh(v19)
        v21 = torch.bmm(v20, v19)
        v22 = torch.tanh(v21)
        v23 = torch.bmm(v22, v21)
        v24 = torch.tanh(v23)
        return v24



func = Model().to('cpu')


x1 = torch.randn(1, 16, 15, 15)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
softmax() received an invalid combination of arguments - got (Tensor), but expected one of:
 * (Tensor input, int dim, torch.dtype dtype = None, *, Tensor out = None)
 * (Tensor input, name dim, *, torch.dtype dtype = None)


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpfi3s3ie4/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpfi3s3ie4/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpfi3s3ie4', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
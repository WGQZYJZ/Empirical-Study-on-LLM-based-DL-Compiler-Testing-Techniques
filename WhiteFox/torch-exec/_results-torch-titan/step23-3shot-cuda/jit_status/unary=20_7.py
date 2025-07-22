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



class MyModel(torch.nn.Module):

    def __init__(self):
        super().__init__()
        kernel_size = 2
        stride = 2
        padding = 1
        self.t_conv = nn.ConvTranspose2d(in_channels=8, out_channels=8, kernel_size=kernel_size, stride=stride, padding=padding)
        self.sig = nn.Sigmoid()

    def forward(self, x1):
        x1 = self.t_conv(x1)
        x2 = self.sig(x1)
        return x2



func = MyModel().to('cuda')



x1 = torch.randn(1, 8, 128, 128)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp5er93pk5/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp5er93pk5', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp5er93pk5/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
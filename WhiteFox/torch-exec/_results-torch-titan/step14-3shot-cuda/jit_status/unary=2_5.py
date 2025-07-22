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
        self.conv_transpose = torch.nn.ConvTranspose2d(12, 48, kernel_size=3, stride=1, padding=1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(48, 36, kernel_size=5, stride=1, padding=2)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(36, 24, kernel_size=3, stride=2, padding=1)
        self.conv_transpose4 = torch.nn.ConvTranspose2d(24, 12, kernel_size=5, stride=2, padding=2)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 * 0.5)
        v3 = ((v1 * v1) * v1)
        v4 = (v3 * 0.044715)
        v5 = (v1 + v4)
        v6 = (v5 * 0.7978845608028654)
        v7 = torch.tanh(v6)
        v8 = (v7 + 1)
        v9 = (v2 * v8)
        v10 = self.conv_transpose2(v9)
        v11 = self.conv_transpose3(v10)
        v12 = self.conv_transpose4(v11)
        return v12




func = Model().to('cuda')



x1 = torch.randn(1, 12, 12, 12)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpu95b8hcs/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpu95b8hcs', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpu95b8hcs/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
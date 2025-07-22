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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(29, 26, 4, padding=2, stride=2)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(26, 27, 1, padding=0, stride=1)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(27, 28, 1, padding=0, stride=1)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = self.conv_transpose2(v1)
        v3 = (v2 * 0.5)
        v4 = ((v2 * v2) * v2)
        v5 = (v4 * 3.9774841810124675e-05)
        v6 = (v2 + v5)
        v7 = torch.tanh(v6)
        v8 = (v7 + 1)
        v9 = (v3 * v8)
        v10 = self.conv_transpose3(v9)
        return v10




func = Model().to('cuda')



x1 = torch.randn(12, 29, 3, 7)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpm2e7cgfc/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpm2e7cgfc', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpm2e7cgfc/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
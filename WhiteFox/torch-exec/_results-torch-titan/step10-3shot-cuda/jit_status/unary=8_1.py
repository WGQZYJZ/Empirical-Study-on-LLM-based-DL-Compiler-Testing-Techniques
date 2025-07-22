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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(24, 24, 3, stride=1, padding=0, bias=True, groups=1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(24, 36, 1, stride=1, padding=0, bias=True, groups=1)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(36, 24, 3, stride=2, padding=0, bias=True, groups=1)
        self.conv_transpose4 = torch.nn.ConvTranspose2d(24, 3, 1, stride=2, padding=0, output_padding=1, bias=True, groups=1)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = self.conv_transpose2(v1)
        v3 = self.conv_transpose3(v2)
        v4 = self.conv_transpose4(v3)
        v5 = (v4 + 3)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 24, 30, 30)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp1cdvhr0v/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp1cdvhr0v', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp1cdvhr0v/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
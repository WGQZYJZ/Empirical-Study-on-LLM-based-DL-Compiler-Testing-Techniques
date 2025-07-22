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



class Module_18(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_transpose_21 = torch.nn.ConvTranspose2d(1, 54, 77, stride=2, padding=38, output_padding=1)
        self.conv_6 = torch.nn.Conv2d(54, 2, 7, stride=2, padding=3, dilation=1)

    def forward(self, x1):
        v1 = self.conv_transpose_21(x1)
        v2 = torch.sigmoid(v1)
        v3 = (v1 * v2)
        v4 = self.conv_6(v3)
        return v4




func = Module_18().to('cuda')



x1 = torch.randn(1, 1, 179, 179)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpbdgqafzw/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpbdgqafzw', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpbdgqafzw/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
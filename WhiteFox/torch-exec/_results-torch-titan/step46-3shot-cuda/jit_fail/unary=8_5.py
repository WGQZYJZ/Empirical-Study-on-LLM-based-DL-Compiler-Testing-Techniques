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
        self.conv = torch.nn.Conv2d(2, 4, 3, stride=2, padding=1, bias=False)
        self.conv_transpose1 = torch.nn.ConvTranspose2d(4, 8, 3, stride=2, padding=1, dilation=1, output_padding=1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(8, 4, 3, stride=1, padding=1, dilation=1, output_padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv_transpose1(v1)
        v2 = self.conv_transpose2(v2)
        v3 = (v2 + 3)
        v4 = torch.clamp(v3, min=0)
        v5 = torch.clamp(v4, max=6)
        v6 = (v2 * v5)
        v7 = (v6 / 6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 2, 7, 7, requires_grad=True)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_height: 1 output_padding_width: 1 stride_height: 1 stride_width: 1 dilation_height: 1 dilation_width: 1

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpix99mf17/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpix99mf17', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpix99mf17/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
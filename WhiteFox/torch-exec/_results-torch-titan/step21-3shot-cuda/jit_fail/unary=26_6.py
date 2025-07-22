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
        self.conv_t = torch.nn.ConvTranspose2d(8, 8, 3, stride=1, padding=1, output_padding=2, dilation=2, groups=2)

    def forward(self, x3):
        t1 = self.conv_t(x3)
        x4 = (t1 > 0)
        x5 = (t1 * 0.294378)
        x6 = torch.where(x4, t1, x5)
        return x6




func = Model().to('cuda')



x3 = torch.randn(16, 8, 20, 20)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_height: 2 output_padding_width: 2 stride_height: 1 stride_width: 1 dilation_height: 2 dilation_width: 2

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpkwm48bdp/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpkwm48bdp', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpkwm48bdp/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
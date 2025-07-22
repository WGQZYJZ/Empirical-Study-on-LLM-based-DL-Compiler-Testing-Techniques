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
        self.conv_transpose_1 = torch.nn.ConvTranspose1d(1, 9, 3, stride=2, output_padding=(1, 1))
        self.conv_transpose_2 = torch.nn.ConvTranspose1d(9, 1, 3, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose_1(x1)
        v2 = self.conv_transpose_2(v1)
        v3 = (v2 + 1)
        v4 = torch.clamp_min(v3, 0)
        v5 = torch.clamp_max(v4, 6)
        v5 = torch.div(v5, 6)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 1, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
expected output_padding to be a single integer value or a list of 1 values to match the convolution dimensions, but got output_padding=[1, 1]

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpfzoch0bk/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpfzoch0bk', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpfzoch0bk/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
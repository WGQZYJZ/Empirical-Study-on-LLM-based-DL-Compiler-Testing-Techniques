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
        self.conv1_transpose = torch.nn.ConvTranspose2d(in_channels=17, out_channels=4, kernel_size=(3, 5), stride=(3, 4), padding=(1, 2), dilation=2, output_padding=3)
        self.conv2_transpose = torch.nn.ConvTranspose2d(in_channels=4, out_channels=9, kernel_size=(5, 3), stride=(2, 2), padding=(2, 1), dilation=2, output_padding=1)

    def forward(self, x1):
        v1 = self.conv1_transpose(x1)
        v2 = (v1 + 3)
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = (v1 * v4)
        v6 = (v5 / 6)
        v7 = self.conv2_transpose(v6)
        v8 = (v7 + 3)
        v9 = torch.clamp(v8, min=0)
        v10 = torch.clamp(v9, max=6)
        v11 = (v7 * v10)
        v12 = (v11 / 6)
        return v12




func = Model().to('cuda')



x1 = torch.randn(1, 17, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
output padding must be smaller than either stride or dilation, but got output_padding_height: 3 output_padding_width: 3 stride_height: 3 stride_width: 4 dilation_height: 2 dilation_width: 2

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpl6g42yz1/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpl6g42yz1', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpl6g42yz1/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
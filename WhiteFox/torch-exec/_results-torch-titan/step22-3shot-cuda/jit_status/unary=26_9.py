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

    def __init__(self, stride, padding, output_padding):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(15, 16, (2, 2), stride, padding=padding, output_padding=output_padding)

    def forward(self, x3):
        v1 = self.conv_t(x3)
        v2 = (v1 > 5.784)
        v3 = (v1 * 2.428)
        v4 = torch.where(v2, v1, v3)
        return v4




stride = 2


padding = 0


output_padding = 0


func = Model(stride, padding, output_padding).to('cuda')



x3 = torch.randn(16, 15, 8, 8)


test_inputs = [x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp1z48orrs/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp1z48orrs', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp1z48orrs/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
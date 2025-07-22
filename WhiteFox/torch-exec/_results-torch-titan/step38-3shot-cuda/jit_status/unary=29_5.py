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

    def __init__(self, min_value=0.6381):
        super().__init__()
        self.leaky_relu = torch.nn.LeakyReLU(3.9523)
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 17, 1, stride=1, padding=0, dilation=2, output_padding=0)
        self.min_value = min_value

    def forward(self, x9):
        v1 = self.conv_transpose(x9)
        v2 = torch.clamp_min(v1, self.min_value)
        return v2




func = Model().to('cuda')



x9 = torch.randn(1, 3, 128, 128)


test_inputs = [x9]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpvfdy4win/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpvfdy4win', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpvfdy4win/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
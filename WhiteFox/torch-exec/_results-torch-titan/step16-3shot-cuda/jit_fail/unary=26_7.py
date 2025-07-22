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

    def __init__(self, negative_slope):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose1d(14, 25, 1, stride=1, padding=0)
        self.negative_slope = negative_slope

    def forward(self, x3):
        v1 = self.conv_t(x3)
        v2 = (v1 > 0)
        v3 = (v1 * self.negative_slope)
        v4 = torch.where(v2, v1, v3)
        return v4




negative_slope = 0.01


func = Model(negative_slope).to('cuda')



x3 = torch.randn(8, 25, 5)


test_inputs = [x3]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [14, 25, 1], expected input[8, 25, 5] to have 14 channels, but got 25 channels instead

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpe15ole8z/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpe15ole8z', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpe15ole8z/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
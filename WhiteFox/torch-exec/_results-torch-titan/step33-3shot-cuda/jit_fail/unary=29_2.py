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

    def __init__(self, min_value=0.4, max_value=0.5):
        super().__init__()
        self.softmax = torch.nn.Softmax(dim=(- 1))
        self.conv_transpose = torch.nn.ConvTranspose1d(10, 10, 1, stride=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.softmax(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(4, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Given transposed=1, weight of size [10, 10, 1], expected input[1, 4, 10] to have 10 channels, but got 4 channels instead

jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp034jrhiw/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp034jrhiw', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp034jrhiw/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def __init__(self, min_value=1.5, max_value=3.8):
        super().__init__()
        self.leaky_relu = torch.nn.LeakyReLU()
        self.zero_pad2d = torch.nn.ZeroPad2d(1)
        self.constant_pad_nd = torch.nn.ConstantPad3d(2, 2)
        self.max_pool2d = torch.nn.MaxPool2d(3, stride=2, padding=0)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.max_pool2d(x1)
        v2 = self.constant_pad_nd(v1)
        v3 = self.max_pool2d(v2)
        v4 = self.max_pool2d(v3)
        v5 = self.leaky_relu(v4)
        v6 = self.max_pool2d(v5)
        v7 = self.constant_pad_nd(v6)
        v8 = self.zero_pad2d(v7)
        v9 = torch.clamp_max(v8, self.max_value)
        return v9




func = Model().to('cuda')



x1 = torch.randn(2, 6, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpqwmwgd3a/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpqwmwgd3a', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpqwmwgd3a/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
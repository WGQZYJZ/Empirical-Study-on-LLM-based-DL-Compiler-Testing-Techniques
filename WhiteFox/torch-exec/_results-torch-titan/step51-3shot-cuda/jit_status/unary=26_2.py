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
        self.conv_t = torch.nn.ConvTranspose2d(10, 10, 7, stride=1, padding=0)
        self.max_pool2d = torch.nn.MaxPool2d(kernel_size=[3, 3], stride=[1, 1], padding=0, dilation=1, ceil_mode=False)
        self.negative_slope = negative_slope

    def forward(self, x2):
        v1 = self.conv_t(x2)
        v4 = self.max_pool2d(v1)
        v6 = (v4 > 0)
        v7 = (v4 * self.negative_slope)
        v8 = torch.where(v6, v4, v7)
        return v8




negative_slope = (- 2.8388)


func = Model(negative_slope).to('cuda')



x2 = torch.randn(22, 10, 6, 6)


test_inputs = [x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp8w36hm4l/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp8w36hm4l', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp8w36hm4l/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
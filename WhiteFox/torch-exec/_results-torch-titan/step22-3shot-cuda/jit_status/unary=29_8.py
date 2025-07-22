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

    def __init__(self, min_value, max_value):
        super(Model, self).__init__()
        self.leaky_relu = torch.nn.LeakyReLU()
        self.max_pool2d = torch.nn.MaxPool2d(8, stride=2, padding=1)
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 32, 8, stride=2, padding=3)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x3):
        v1 = self.conv_transpose(x3)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.leaky_relu(v3)
        v5 = self.max_pool2d(v4)
        return v5




min_value = (- 0.5)


max_value = 0.5


func = Model(min_value, max_value).to('cuda')



x3 = torch.randn(1, 3, 224, 256)


test_inputs = [x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpov9dmqeg/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpov9dmqeg', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpov9dmqeg/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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

    def __init__(self, min_value=2.6, max_value=6.9):
        super().__init__()
        self.transpose_conv2d_1 = torch.nn.ConvTranspose2d(2, 10, 1, stride=1, padding=0)
        self.act_2 = torch.nn.ReLU6()
        self.transpose_conv2d_2 = torch.nn.ConvTranspose2d(10, 10, 1, stride=1, padding=0)
        self.act_5 = torch.nn.ReLU()
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x2):
        v1 = self.transpose_conv2d_1(x2)
        v2 = (v1 + (- 2.648787352965254))
        v3 = torch.clamp_min(v2, self.min_value)
        v4 = torch.clamp_max(v3, self.max_value)
        v5 = self.act_2(v4)
        v6 = self.transpose_conv2d_2(v5)
        v7 = torch.clamp_min(v6, self.min_value)
        v8 = torch.clamp_max(v7, self.max_value)
        v9 = self.act_5(v8)
        return v9




func = Model().to('cuda')



x2 = torch.randn(1, 2, 224, 224)


test_inputs = [x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpc0mbizv7/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpc0mbizv7', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpc0mbizv7/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
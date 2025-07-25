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

    def __init__(self, min_value=(- 0.3), max_value=1.3):
        super(Model, self).__init__()
        self.softsign = torch.nn.Softsign()
        self.batch_norm = torch.nn.BatchNorm2d(16)
        self.conv_transpose = torch.nn.ConvTranspose2d(10, 16, 1, stride=1, padding=1)
        self.act_10 = torch.nn.LeakyReLU()
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x4):
        v1 = self.conv_transpose(x4)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.softsign(v3)
        v9 = self.act_10(v4)
        return v9




func = Model().to('cuda')



x5 = torch.randn(1, 10, 124, 124)


test_inputs = [x5]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpnoijv6px/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpnoijv6px', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpnoijv6px/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
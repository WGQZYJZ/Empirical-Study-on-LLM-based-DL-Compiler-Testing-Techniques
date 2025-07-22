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

    def __init__(self, min_value=3.2, max_value=3.2):
        super(Model, self).__init__()
        self.softsign = torch.nn.Softsign()
        self.leaky_relu = torch.nn.LeakyReLU()
        self.max_pool2d = torch.nn.MaxPool2d(2, stride=2, padding=0)
        self.conv2d = torch.nn.Conv2d(8, 18, 3, stride=1, padding=1)
        self.act_4 = torch.nn.Tanh()
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x3):
        v1 = self.conv2d(x3)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        v4 = self.softsign(v3)
        v9 = self.leaky_relu(v4)
        v11 = self.max_pool2d(v9)
        v13 = self.act_4(v11)
        return v13




func = Model().to('cuda')



x3 = torch.randn(1, 8, 224, 224)


test_inputs = [x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpgup2cq8m/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpgup2cq8m', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpgup2cq8m/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
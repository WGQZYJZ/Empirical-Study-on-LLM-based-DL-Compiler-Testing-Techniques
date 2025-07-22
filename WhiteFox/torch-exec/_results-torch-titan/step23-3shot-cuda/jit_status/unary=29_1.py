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

    def __init__(self, min_value=(- 0.9), max_value=0.9):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=2, padding=0)
        self.bn = torch.nn.BatchNorm2d(num_features=8)
        self.tanh = torch.nn.Tanh()
        self.act_1 = torch.nn.ReLU6()
        self.max_pool2d = torch.nn.MaxPool2d(2, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.bn(v1)
        v5 = self.act_1(v2)
        v8 = self.max_pool2d(v5)
        v9 = torch.clamp_min(v8, self.min_value)
        v10 = torch.clamp_max(v9, self.max_value)
        v11 = self.tanh(v10)
        return v11




func = Model().to('cuda')



x1 = torch.randn(1, 3, 112, 112)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp2dnrogq7/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp2dnrogq7', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp2dnrogq7/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
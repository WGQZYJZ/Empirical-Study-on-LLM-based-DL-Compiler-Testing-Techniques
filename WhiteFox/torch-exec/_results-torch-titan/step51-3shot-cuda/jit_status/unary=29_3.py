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

    def __init__(self, min_value=0.1, max_value=0.2):
        super().__init__()
        self.max_pool2d = torch.nn.MaxPool2d(2, stride=1)
        self.dropout = torch.nn.Dropout()
        self.conv_transpose = torch.nn.ConvTranspose2d(12, 8, 3, stride=3, padding=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x4):
        v1 = self.max_pool2d(x4)
        v2 = self.dropout(v1)
        v3 = self.conv_transpose(v2)
        v4 = torch.clamp_min(v3, self.min_value)
        v5 = torch.clamp_max(v4, self.max_value)
        return v5




func = Model().to('cuda')



x4 = torch.randn(1, 12, 11, 21)


test_inputs = [x4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpzc93eqw5/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpzc93eqw5', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpzc93eqw5/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
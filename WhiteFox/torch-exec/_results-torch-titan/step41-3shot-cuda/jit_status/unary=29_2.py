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

    def __init__(self, min_value=(- 60.82), max_value=32):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 5, 1, stride=1, padding=1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(5, 9, 1, stride=1, padding=1)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(9, 13, 1, stride=1, padding=1)
        self.avg_pool2d = torch.nn.AvgPool2d(2)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.conv_transpose2(v1)
        v3 = self.conv_transpose3(v2)
        v4 = self.avg_pool2d(v3)
        v5 = v4.view(v4.size(0), (- 1))
        v6 = torch.clamp_min(v5, self.min_value)
        v7 = torch.clamp_max(v6, self.max_value)
        v8 = torch.reshape(v7, v4.shape)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 1, 16, 16)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp2r56x1_a/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp2r56x1_a', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp2r56x1_a/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
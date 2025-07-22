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

    def __init__(self, min_value=(- 0.1332), max_value=(- 1.1488)):
        super().__init__()
        self.relu = torch.nn.ReLU(inplace=False)
        self.batch_normalization = torch.nn.BatchNorm2d(47, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
        self.conv_transpose2d_1 = torch.nn.ConvTranspose2d(47, 16, (1, 5), stride=1, padding=0, output_padding=0, groups=1, bias=True, dilation=1)
        self.conv_transpose2d_2 = torch.nn.ConvTranspose2d(16, 2, 5, stride=1, padding=0, output_padding=0, groups=1, bias=True, dilation=1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x8):
        v5 = self.batch_normalization(x8)
        v8 = self.relu(v5)
        v10 = self.conv_transpose2d_1(v8)
        v11 = self.relu(v10)
        v12 = self.conv_transpose2d_2(v11)
        v13 = torch.clamp_min(v12, self.min_value)
        v14 = torch.clamp_max(v13, self.max_value)
        return v14




func = Model().to('cuda')



x8 = torch.randn(1, 47, 28, 8)


test_inputs = [x8]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpqckn_e8o/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpqckn_e8o', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpqckn_e8o/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
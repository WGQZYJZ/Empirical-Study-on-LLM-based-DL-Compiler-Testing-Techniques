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

    def __init__(self):
        super().__init__()
        self.depthwise_conv1 = torch.nn.Conv2d(in_channels=1, out_channels=8, kernel_size=3, stride=2, padding=0, dilation=1, groups=1, bias=True)
        self.depthwise_conv2 = torch.nn.Conv2d(in_channels=1, out_channels=8, kernel_size=3, stride=2, padding=0, dilation=1, groups=1, bias=True)

    def forward(self, x1):
        v1 = self.depthwise_conv1(x1)
        v2 = self.depthwise_conv2(x1)
        v3 = self.depthwise_conv1(x1)
        v4 = ((v1 + v2) + v3)
        v5 = torch.relu(v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 1, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpbq0_7tko/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpbq0_7tko', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpbq0_7tko/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
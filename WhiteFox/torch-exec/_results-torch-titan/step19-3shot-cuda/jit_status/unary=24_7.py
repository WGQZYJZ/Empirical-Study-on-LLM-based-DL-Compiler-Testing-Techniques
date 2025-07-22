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

    def __init__(self, channels=8, input_shape=(64, 64)):
        super().__init__()
        (width, height) = input_shape
        self.conv = torch.nn.Conv2d(channels, channels, 3, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(channels)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.bn(v1)
        v3 = v2.clone()
        v4 = torch.where((v2 > 1.0), v2, torch.zeros_like(v2))
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 8, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpvdgpco8o/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpvdgpco8o', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpvdgpco8o/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
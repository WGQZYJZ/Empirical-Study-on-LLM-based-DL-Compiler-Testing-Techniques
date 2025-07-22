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

    def __init__(self, negative_slope):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, 32, stride=2, padding=3)
        self.negative_slope = negative_slope

    def forward(self, x):
        v1 = self.negative_slope
        v2 = self.conv(x)
        v3 = (v2 > 0)
        v4 = (v2 * v1)
        v5 = torch.where(v3, v2, v4)
        return v5




negative_slope = 0.1


func = Model(negative_slope).to('cuda')



x1 = torch.randn(1, 1, 128, 128)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpxk2uasle/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpxk2uasle', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpxk2uasle/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
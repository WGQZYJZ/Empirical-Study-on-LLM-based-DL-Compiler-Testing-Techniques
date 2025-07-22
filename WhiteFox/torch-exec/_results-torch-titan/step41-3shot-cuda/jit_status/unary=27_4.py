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

    def __init__(self, min, max, tanh_enabled):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 1, 3, bias=True, padding=1)
        self.relu = torch.nn.ReLU(inplace=True)
        self.tanh = torch.nn.Tanh()
        self.sigmoid = torch.nn.Sigmoid()
        self.min = min
        self.max = max
        self.tanh_enabled = tanh_enabled

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min)
        v3 = torch.clamp_max(v2, self.max)
        if self.tanh_enabled:
            v4 = self.tanh(v3)
        else:
            v4 = self.sigmoid(v3)
        return v4




min = 0


max = 2


tanh_enabled = False


func = Model(min, max, tanh_enabled).to('cuda')



x1 = torch.randn(1, 1, 2, 2)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpvka_vnvh/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpvka_vnvh', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpvka_vnvh/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
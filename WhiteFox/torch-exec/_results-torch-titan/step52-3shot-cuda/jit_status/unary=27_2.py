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

    def __init__(self, min, max, min_1, max_1):
        super().__init__()
        self.min = min
        self.max = max
        self.conv = torch.nn.Conv3d(1, 7, 7, stride=2, padding=3)
        self.min_1 = min_1
        self.max_1 = max_1

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min)
        v3 = torch.clamp_max(v2, self.max)
        v4 = F.relu(v3)
        v5 = torch.clamp_min(v4, self.min_1)
        v6 = torch.clamp_max(v5, self.max_1)
        return v6




min = 5.9


max = 6.6


min_1 = (- 3.3)


max_1 = 7.5


func = Model(min, max, min_1, max_1).to('cuda')



x1 = torch.randn(1, 1, 80, 80, 80)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_083wdhv/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp_083wdhv', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp_083wdhv/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
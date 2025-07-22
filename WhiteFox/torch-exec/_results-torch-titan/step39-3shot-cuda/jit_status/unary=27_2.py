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

    def __init__(self, min, max, min_2, max_2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 5, stride=1, padding=2)
        self.min = min
        self.max = max
        self.min_2 = min_2
        self.max_2 = max_2

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min)
        v3 = torch.clamp_max(v2, self.max)
        v4 = torch.clamp_min(v3, self.min_2)
        v5 = torch.clamp_max(v4, self.max_2)
        return v5




min = 1


max = 0


min_2 = 1


max_2 = 0


func = Model(min, max, min_2, max_2).to('cuda')



x1 = torch.randn(1, 3, 100, 200)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpd7_zvu70/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpd7_zvu70', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpd7_zvu70/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
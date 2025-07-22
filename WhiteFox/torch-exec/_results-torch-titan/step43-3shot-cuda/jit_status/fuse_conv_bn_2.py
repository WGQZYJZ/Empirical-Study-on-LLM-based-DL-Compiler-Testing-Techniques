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
        torch.manual_seed(1)
        y1 = torch.zeros(3, 3).float()
        torch.manual_seed(1)
        y2 = torch.zeros(3, 3).float()
        torch.manual_seed(1)
        self.conv = torch.nn.Conv2d(1, 1, 1, bias=True)
        self.bn = torch.nn.BatchNorm2d(1, track_running_stats=True, affine=True)

    def forward(self, x1):
        s1 = self.conv(x1)
        s1 = self.bn(s1)
        s1 = self.conv(s1)
        s1 = self.bn(s1)
        return s1




func = Model().to('cuda')



x1 = torch.randn(1, 1, 4, 4)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpyrf10tfg/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpyrf10tfg', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpyrf10tfg/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
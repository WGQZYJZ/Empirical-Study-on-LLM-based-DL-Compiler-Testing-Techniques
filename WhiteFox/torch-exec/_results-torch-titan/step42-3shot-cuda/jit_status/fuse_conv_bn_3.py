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
        self.a = torch.nn.Conv2d(3, 3, 3, groups=1, bias=False)
        self.b = torch.nn.BatchNorm2d(3, momentum=0.1, affine=True, track_running_stats=True)
        self.c = torch.nn.Conv2d(3, 3, 3, stride=1, dilation=1, groups=1, bias=False, padding=1)

    def forward(self, x):
        o1 = self.a(x)
        o2 = self.b(o1)
        o3 = self.c(o2)
        return o3




func = Model().to('cuda')



x = torch.randn(1, 3, 3, 3)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpsy0xakpr/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpsy0xakpr', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpsy0xakpr/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
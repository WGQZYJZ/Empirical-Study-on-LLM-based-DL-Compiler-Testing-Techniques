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
        self.conv1 = torch.nn.Conv2d(10, 3, 7, stride=2, padding=3, groups=1)
        self.conv2 = torch.nn.Conv2d(3, 1, 7, stride=2, padding=3, groups=1)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = torch.nn.functional.interpolate(v1, size=[64, 64], mode='bilinear', align_corners=False)
        v3 = self.conv2(v2)
        v4 = torch.nn.functional.interpolate(v3, size=[64, 64], mode='bilinear', align_corners=False)
        return v4




func = Model().to('cuda')



x = torch.randn(1, 10, 64, 64)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpa2a4tcsw/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpa2a4tcsw', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpa2a4tcsw/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
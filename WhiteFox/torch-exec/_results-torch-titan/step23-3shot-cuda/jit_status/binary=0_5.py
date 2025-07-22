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



class Model1(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=2, padding=0)

    def forward(self, x1, x2, other1=1, other2=1):
        v1 = self.conv(x1)
        v2 = (v1 + other1)
        v3 = torch.cat((v2, x2), dim=1)
        return v3




class Model2(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 3, 3, stride=3, padding=4)

    def forward(self, x1, x2, other1=1, other2=1):
        v1 = self.conv(x1)
        v2 = (x1 + other2)
        v3 = (v1 + other1)
        return v3




func = Model2().to('cuda')



x1 = torch.randn(1, 3, 16, 16)



x2 = torch.randn(1, 3, 14, 14)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpv6g2nu6e/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpv6g2nu6e', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpv6g2nu6e/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv = torch.nn.Conv2d(3, 64, 1, stride=2, padding=2)
        self.conv_next = torch.nn.Conv2d(64, 16, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = F.sigmoid(x1)
        v1 = v1.mul(x1)
        v2 = self.conv(v1)
        v3 = F.sigmoid(v2)
        v3 = v2.mul(v3)
        v4 = v2.add(v3)
        v5 = self.conv_next(v4)
        v6 = F.sigmoid(v5)
        v6 = v5.mul(v6)
        return v6




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpffby_t4r/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpffby_t4r', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpffby_t4r/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
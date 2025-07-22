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
        self.conv = torch.nn.Conv2d(2, 3, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = (v1 + 3)
        v3 = F.hardtanh(v2, min_val=0.0, max_val=6.0)
        v4 = torch.clamp(v3, 0, 6)
        v5 = (v1 * v4)
        v6 = (v5 / 6)
        c1 = self.conv(x2)
        c2 = (c1 + 3)
        c3 = F.hardtanh(c2, min_val=0.0, max_val=6.0)
        c4 = torch.clamp(c3, 0, 6)
        c5 = (c1 * c4)
        c6 = (c5 / 6)
        return (v6 + c6)




func = Model().to('cuda')



x1 = torch.randn(1, 2, 64, 64)



x2 = torch.randn(1, 2, 64, 64)


test_inputs = [x1, x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpmqrm33pz/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpmqrm33pz', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpmqrm33pz/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
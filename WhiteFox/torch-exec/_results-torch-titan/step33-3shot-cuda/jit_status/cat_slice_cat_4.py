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
        self.conv1 = torch.nn.Conv2d(3, 64, 7, stride=2, padding=3)
        self.conv2 = torch.nn.Conv2d(64, 128, 7, stride=2, padding=3)
        self.conv3 = torch.nn.Conv2d(128, 256, 7, stride=2, padding=3)
        self.conv4 = torch.nn.Conv2d(256, 512, 7, stride=2, padding=3)

    def forward(self, x1):
        v1 = F.relu_(self.conv1(x1))
        v2 = F.relu_(self.conv2(v1))
        out = F.relu_(self.conv3(v2))
        out1 = F.relu_(self.conv4(out))
        return out1



func = Model().to('cuda')



input = torch.randn(3, 3, 64, 64)


test_inputs = [input]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpf5vzprii/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpf5vzprii', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpf5vzprii/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
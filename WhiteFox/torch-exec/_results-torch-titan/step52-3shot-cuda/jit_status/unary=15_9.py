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
        self.conv1 = torch.nn.Conv2d(3, 64, 3, stride=1, padding=1, bias=False)
        self.norm1 = torch.nn.BatchNorm2d(64, eps=0.001, momentum=0.010000000000000009, affine=True)
        self.relu1 = torch.nn.ReLU(inplace=True)
        self.conv2 = torch.nn.Conv2d(64, 64, 3, stride=1, padding=1, bias=False)
        self.norm2 = torch.nn.BatchNorm2d(64, eps=0.001, momentum=0.010000000000000009, affine=True)
        self.relu2 = torch.nn.ReLU(inplace=True)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.norm1(v1)
        v3 = self.relu1(v2)
        v4 = self.conv2(v3)
        v5 = self.norm2(v4)
        v6 = self.relu2(v5)
        return v6




func = Model().to('cuda')



x1 = torch.randn(3, 3, 640, 640)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmphmwgz3hg/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmphmwgz3hg', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmphmwgz3hg/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
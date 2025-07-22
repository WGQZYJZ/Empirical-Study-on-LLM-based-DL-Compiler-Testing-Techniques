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
        self.block0_conv1 = torch.nn.Conv2d(3, 3, 1, stride=2, padding=0)
        self.block0_bn1 = torch.nn.BatchNorm2d(3, 0.8999999761581421, 0.0, True)
        self.block0_conv2 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=0)
        self.block0_bn2 = torch.nn.BatchNorm2d(3, 0.8999999761581421, 0.0, True)
        self.block0_conv3 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=0)
        self.block0_bn3 = torch.nn.BatchNorm2d(3, 0.8999999761581421, 0.0, True)

    def forward(self, x1):
        v1 = self.block0_conv1(x1)
        v2 = self.block0_bn1(v1)
        v2 = F.relu(v2)
        v1 = self.block0_conv2(v2)
        v2 = self.block0_bn2(v1)
        v2 = F.relu(v2)
        v3 = self.block0_conv3(v2)
        v4 = self.block0_bn3(v3)
        v5 = F.max_pool2d(v4, 2, 2)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 288, 288)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpijhril58/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpijhril58', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpijhril58/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
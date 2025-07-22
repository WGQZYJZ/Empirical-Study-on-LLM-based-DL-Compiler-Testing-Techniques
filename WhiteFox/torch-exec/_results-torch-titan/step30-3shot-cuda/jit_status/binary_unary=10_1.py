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
        self.bn0 = torch.nn.BatchNorm2d(3)
        self.l1 = torch.nn.Conv2d(3, 4, 7, stride=2, padding=0)
        self.bn1 = torch.nn.BatchNorm2d(4)
        self.l2 = torch.nn.Conv2d(4, 6, 3, stride=1, padding=0)
        self.bn2 = torch.nn.BatchNorm2d(6)
        self.l3 = torch.nn.Conv2d(6, 20, 1, stride=1, padding=0)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        v1 = self.l1(x)
        v2 = self.bn1(v1)
        v3 = self.l2(v2)
        v4 = self.bn2(v3)
        v5 = self.l3(v4)
        v6 = v5.mean([2, 3])
        v7 = self.relu(v6)
        return v7



func = Model().to('cuda')



x1 = torch.randn(100, 3, 224, 224)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmprwxub4nf/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmprwxub4nf', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmprwxub4nf/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv1 = torch.nn.Conv2d(4, 13, 1, stride=1, padding=0)
        self.t1 = torch.nn.Tanh()
        self.conv2 = torch.nn.Conv2d(13, 3072, 11, stride=11, padding=0)
        self.t2 = torch.nn.Tanh()
        self.conv3 = torch.nn.Conv2d(3072, 1000, 1, stride=1, padding=0)
        self.t3 = torch.nn.Tanh()

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.t1(v1)
        v3 = self.conv2(v2)
        v4 = self.t2(v3)
        v5 = self.conv3(v4)
        v6 = self.t3(v5)
        return v6




func = Model().to('cuda')



x = torch.randn(1, 4, 318, 255)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpycolhr9_/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpycolhr9_', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpycolhr9_/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
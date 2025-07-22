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
        torch.manual_seed(8)
        self.m1 = torch.nn.Sequential(torch.nn.Conv2d(2, 2, 2, bias=False), torch.nn.BatchNorm2d(2))
        self.m2 = torch.nn.Sequential(torch.nn.Conv2d(2, 2, 2, bias=False), torch.nn.Sigmoid())

    def forward(self, x4):
        t = self.m1(x4)
        t2 = self.m2(t)
        return t2




func = Model().to('cuda')



x4 = torch.randn(1, 2, 4, 4)


test_inputs = [x4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpny2dcvsl/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpny2dcvsl', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpny2dcvsl/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
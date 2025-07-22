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
        super(Model, self).__init__()
        self.t1 = torch.nn.ConvTranspose2d(95, 173, 2, stride=1, padding=1, bias=False)
        self.acti1 = torch.nn.ReLU(inplace=False)
        self.t2 = torch.nn.ConvTranspose2d(173, 93, 2, stride=1, padding=1, bias=False)
        self.acti2 = torch.nn.Identity()
        self.t3 = torch.nn.ConvTranspose2d(93, 1, 3, stride=1, padding=1, bias=False)
        self.acti3 = torch.nn.Sigmoid()

    def forward(self, x3):
        x1 = self.t1(x3)
        x4 = self.acti1(x1)
        x5 = self.t2(x4)
        x7 = self.acti2(x5)
        x6 = self.t3(x7)
        x8 = self.acti3(x6)
        return x8




func = Model().to('cuda')



x3 = torch.randn(16, 95, 8, 9)


test_inputs = [x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpdazctld8/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpdazctld8', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpdazctld8/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
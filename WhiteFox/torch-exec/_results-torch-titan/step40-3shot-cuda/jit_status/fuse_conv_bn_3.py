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
        self.main_encoder = torch.nn.Sequential()
        self.main_encoder.add_module('layers0', torch.nn.Sequential(torch.nn.Conv2d(3, 3, 1, 1, 4)))
        self.main_encoder.add_module('layers1', torch.nn.Sequential(torch.nn.ReLU(True)))

    def forward(self, x):
        o = self.main_encoder(x)
        o = (o + o)
        o = (o + o)
        o = (o + o)
        return o




func = Model().to('cuda')



x1 = torch.randn(3, 3, 1, 1)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp936i9mc_/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp936i9mc_', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp936i9mc_/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
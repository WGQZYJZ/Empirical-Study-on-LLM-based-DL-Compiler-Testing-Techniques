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
        self.block0 = torch.nn.Sequential(torch.nn.Conv2d(512, 512, 3), torch.nn.ReLU(), torch.nn.BatchNorm2d(512, 0.8), torch.nn.Conv2d(512, 512, 1))
        self.relu = torch.nn.ReLU()

    def forward(self, x3):
        y0 = self.block0(x3)
        y = self.relu(y0)
        return y




func = Model().to('cuda')



x3 = torch.randn(1, 512, 30, 30)


test_inputs = [x3]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpueqiek_d/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpueqiek_d', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpueqiek_d/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
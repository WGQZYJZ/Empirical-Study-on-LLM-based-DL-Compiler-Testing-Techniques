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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(18, 4, 3, stride=1, padding=1)
        self.pool = torch.nn.MaxPool2d(3, stride=3)
        self.conv2 = torch.nn.Conv2d(12, 1, 1, stride=1, padding=1)

    def forward(self, x):
        v1 = torch.tanh(self.conv(x))
        return torch.tanh(self.pool(v1))




func = ModelTanh().to('cuda')



x = torch.randn(1, 18, 64, 64)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp43la9syy/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp43la9syy', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp43la9syy/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
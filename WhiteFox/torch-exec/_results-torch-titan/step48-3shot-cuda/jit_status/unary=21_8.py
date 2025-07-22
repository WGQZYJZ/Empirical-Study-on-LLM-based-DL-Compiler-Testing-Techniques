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
        self.conv = torch.nn.Conv2d(47, 9, 1)
        self.conv1 = torch.nn.Conv2d(9, 1, 1)
        self.conv2 = torch.nn.Conv2d(1, 47, 1)
        self.conv3 = torch.nn.Conv2d(47, 1, 1)
        self.conv4 = torch.nn.Conv2d(1, 32, 3, padding=0)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.tanh(v1)
        v3 = self.conv1(v2)
        v4 = torch.tanh(v3)
        v5 = self.conv2(v4)
        v6 = torch.tanh(v5)
        v7 = self.conv3(v6)
        v8 = torch.tanh(v7)
        v9 = self.conv4(v8)
        return v9




func = ModelTanh().to('cuda')



x = torch.randn(1, 47, 56, 61)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpwo8sbtw2/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpwo8sbtw2', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpwo8sbtw2/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
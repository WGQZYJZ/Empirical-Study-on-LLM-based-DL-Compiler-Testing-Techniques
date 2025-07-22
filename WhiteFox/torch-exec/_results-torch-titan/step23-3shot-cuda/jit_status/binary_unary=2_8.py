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
        self.conv1 = torch.nn.Conv2d(3, 10, 5, stride=2, padding=2)
        self.pool1 = torch.nn.AvgPool2d(2, padding=0)
        self.conv2 = torch.nn.Conv2d(10, 16, 5, stride=2, padding=2)
        self.pool2 = torch.nn.AvgPool2d(2, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.pool1(v1)
        v3 = (v2 - 0.5)
        v4 = self.conv2(v3)
        v5 = self.pool2(v4)
        v6 = (v5 - 1)
        v7 = F.relu(v6)
        v8 = torch.squeeze(v7, 0)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 3, 224, 224)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpcdwar2nn/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpcdwar2nn', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpcdwar2nn/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
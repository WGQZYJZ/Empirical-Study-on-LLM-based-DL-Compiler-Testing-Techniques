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
        self.dropout = torch.nn.Dropout2d()
        self.conv = torch.nn.Conv2d(3, 128, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(128, 10, 1, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(10)
        self.relu = torch.nn.ReLU(inplace=True)

    def forward(self, x1):
        v1 = self.dropout(x1)
        v2 = self.conv(x1)
        v3 = self.conv2(v2)
        v4 = (3 + v3)
        v5 = torch.clamp(v4, 0, 6)
        v6 = (v3 * v5)
        v7 = (v6 / 6)
        v8 = self.bn(v7)
        v9 = self.relu(v8)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 3, 32, 32)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp4q6zgk3k/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp4q6zgk3k', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp4q6zgk3k/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
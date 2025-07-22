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
        self.conv = torch.nn.Conv2d(4, 8, 2, stride=1, padding=0, dilation=1, groups=1)
        self.relu = torch.nn.ReLU(inplace=True)
        self.bn = torch.nn.BatchNorm2d(8)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.relu(v1)
        v3 = self.bn(v2)
        v4 = (v3 * 0.5)
        v5 = (v3 * v3)
        v6 = (v5 * v3)
        v7 = (v6 * 0.044715)
        v8 = (v3 + v7)
        v9 = (v8 * 0.7978845608028654)
        v10 = torch.tanh(v9)
        v11 = (v10 + 1)
        v12 = (v4 * v11)
        return v12




func = Model().to('cuda')



x1 = torch.randn(1, 4, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpcha_rvqa/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpcha_rvqa', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpcha_rvqa/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
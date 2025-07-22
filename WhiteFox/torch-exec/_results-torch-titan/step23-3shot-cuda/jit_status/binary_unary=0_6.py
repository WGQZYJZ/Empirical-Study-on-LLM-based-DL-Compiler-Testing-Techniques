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
        self.conv1 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv2 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)
        self.conv3 = torch.nn.Conv2d(16, 16, 7, stride=1, padding=3)

    def forward(self, x1, x2, x3, x4, x5, x6, x7):
        v1 = self.conv1(x1)
        v2 = (v1 + x2)
        v3 = torch.relu(v2)
        v4 = self.conv2(v3)
        v5 = (v4 + x3)
        v6 = torch.relu(v5)
        v7 = self.conv3(v6)
        v8 = (x4 + x5)
        v9 = (v7 + v8)
        v10 = torch.relu(v9)
        v11 = self.conv2(v10)
        v12 = (v11 + x6)
        v13 = torch.relu(v12)
        v14 = self.conv3(v13)
        v15 = (x7 + v14)
        v16 = torch.relu(v15)
        return v16




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)



x2 = torch.randn(1, 16, 64, 64)



x3 = torch.randn(1, 16, 64, 64)



x4 = torch.randn(1, 16, 64, 64)



x5 = torch.randn(1, 16, 64, 64)



x6 = torch.randn(1, 16, 64, 64)



x7 = torch.randn(1, 16, 64, 64)


test_inputs = [x1, x2, x3, x4, x5, x6, x7]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpns1mpf7o/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpns1mpf7o', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpns1mpf7o/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
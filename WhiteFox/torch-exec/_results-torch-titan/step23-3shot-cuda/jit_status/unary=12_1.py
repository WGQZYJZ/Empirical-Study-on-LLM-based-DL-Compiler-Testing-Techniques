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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, dilation=2)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, dilation=1)
        self.conv3 = torch.nn.Conv2d(8, 8, 1, stride=1, dilation=2)
        self.conv4 = torch.nn.Conv2d(8, 8, 1, stride=1)
        self.conv5 = torch.nn.Conv2d(8, 8, 1, stride=1)
        self.conv6 = torch.nn.Conv2d(8, 8, 1, stride=1)
        self.conv7 = torch.nn.Conv2d(8, 8, 1, stride=1)
        self.conv8 = torch.nn.Conv2d(8, 8, 1, stride=1)
        self.convres = torch.nn.Conv2d(8, 1, 1)
        self.sigmoid1 = torch.nn.Sigmoid()
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        v5 = self.conv5(v4)
        v6 = self.conv6(v5)
        v7 = self.conv7(v6)
        v8 = self.conv8(v7)
        v9 = self.sigmoid1(v8)
        v10 = (v1 * v9)
        v11 = self.convres(v10)
        v12 = self.sigmoid(v11)
        v13 = (v12 * v11)
        return v13




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpdnupv63t/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpdnupv63t', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpdnupv63t/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
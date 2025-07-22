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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=2)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=2)
        self.conv3 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=2)
        self.conv4 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=2)
        self.conv5 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=2)
        self.conv6 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=2)
        self.conv7 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=2)
        self.conv8 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=2)
        self.conv9 = torch.nn.Conv2d(3, 8, 1, stride=2, padding=2)

    def forward(self, x1, x2, x3, x4, x5, x6):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        v3 = self.conv3(x2)
        v4 = self.conv4(x2)
        v5 = self.conv5(x3)
        v6 = self.conv6(x3)
        v7 = self.conv7(x4)
        v8 = self.conv8(x4)
        v9 = self.conv9(x5)
        return v9




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 3, 64, 64)



x3 = torch.randn(1, 3, 64, 64)



x4 = torch.randn(1, 3, 64, 64)



x5 = torch.randn(1, 3, 64, 64)



x6 = torch.randn(1, 3, 64, 64)


test_inputs = [x1, x2, x3, x4, x5, x6]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpnnyl9_81/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpnnyl9_81', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpnnyl9_81/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
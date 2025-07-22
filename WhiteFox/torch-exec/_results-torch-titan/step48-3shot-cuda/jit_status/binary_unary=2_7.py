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
        self.conv1 = torch.nn.Conv2d(3, 10, 11, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(10, 10, 7, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(10, 10, 5, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(10, 10, 3, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = (self.conv2(v1) - 10)
        v3 = torch.relu(v2)
        v4 = (self.conv3(v3) - 10)
        v5 = torch.tanh(v4)
        v6 = (self.conv4(v5) - 10)
        v7 = torch.sigmoid(v6)
        return v7




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpmjz9dbk_/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpmjz9dbk_', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpmjz9dbk_/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
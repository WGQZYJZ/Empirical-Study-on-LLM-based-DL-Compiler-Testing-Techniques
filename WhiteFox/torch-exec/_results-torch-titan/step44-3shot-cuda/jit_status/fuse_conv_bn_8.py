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
        self.conv1 = torch.nn.Conv2d(3, 8, 3, bias=True)
        self.conv2 = torch.nn.Conv2d(8, 8, 2, bias=True)
        self.conv3 = torch.nn.Conv2d(8, 8, 1, bias=True)
        self.relu = torch.nn.ReLU()
        self.layer = torch.nn.Sequential(self.relu, torch.nn.Conv2d(8, 1, 1, bias=True))

    def forward(self, x2):
        s1 = self.conv1(x2)
        s2 = self.relu(s1)
        s3 = self.conv2(s2)
        s4 = self.relu(s3)
        s5 = self.conv3(s4)
        s6 = self.relu(s5)
        s7 = self.layer(s6)
        return s2




func = Model().to('cuda')



x2 = torch.randn(1, 3, 7, 7)


test_inputs = [x2]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpqgjkd068/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpqgjkd068', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpqgjkd068/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
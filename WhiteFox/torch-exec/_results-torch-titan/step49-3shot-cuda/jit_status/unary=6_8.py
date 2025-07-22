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
        self.conv1 = torch.nn.Conv2d(4, 64, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(64, 192, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(192, 1, 1, stride=1, padding=0)
        self.avgpool = torch.nn.AvgPool2d(3, stride=1, padding=1)
        self.relu = torch.nn.ReLU()
        self.tanh = torch.nn.Tanh()

    def forward(self, x1):
        t1 = self.conv1(x1)
        t2 = self.conv2(t1)
        t3 = self.conv3(t2)
        t4 = self.avgpool(t3)
        t5 = self.relu(t4)
        t6 = self.tanh(t5)
        t7 = (t6 - 3)
        t8 = (t6 * 3)
        return t7.unsqueeze((- 1))




func = Model().to('cuda')



x1 = torch.randn(1, 4, 96, 96)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpoyieb4l7/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpoyieb4l7', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpoyieb4l7/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
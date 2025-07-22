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
        self.conv1 = torch.nn.Conv2d(in_channels=69, out_channels=27, kernel_size=3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(in_channels=27, out_channels=10, kernel_size=5, stride=3, padding=4)
        self.conv3 = torch.nn.Conv2d(in_channels=10, out_channels=68, kernel_size=7, stride=7, padding=3)
        self.conv4 = torch.nn.Conv2d(in_channels=68, out_channels=13, kernel_size=1, stride=6, padding=5)

    def forward(self, x1):
        t1 = self.conv1(x1)
        t2 = self.conv2(t1)
        t3 = self.conv3(t2)
        t4 = self.conv4(t3)
        t5 = torch.tanh(t4)
        t6 = torch.sigmoid(t5)
        return t6.flatten()




func = Model().to('cuda')



x1 = torch.randn(1, 69, 100, 100)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp5yce88h3/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp5yce88h3', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp5yce88h3/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
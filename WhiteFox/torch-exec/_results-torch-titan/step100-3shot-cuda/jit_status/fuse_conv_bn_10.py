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
        torch.manual_seed(1)
        self.conv1 = torch.nn.Conv2d(64, 32, 5)
        self.relu1 = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(32, 16, 5)
        self.relu2 = torch.nn.ReLU()
        self.conv3 = torch.nn.Conv2d(16, 16, 5)
        self.activation = torch.sigmoid

    def forward(self, x4):
        y1 = self.conv1(x4)
        y2 = self.relu1(y1)
        y3 = self.conv2(y2)
        y4 = self.relu2(y3)
        y5 = self.conv3(y4)
        y6 = self.activation(y5)
        return y6




func = Model().to('cuda')



x4 = torch.randn(4, 64, 32, 32)


test_inputs = [x4]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp5hcaaee9/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp5hcaaee9', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp5hcaaee9/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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



class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1_1 = torch.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=1, groups=192)
        self.conv1_2 = torch.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=1, groups=192)
        self.conv1_3 = torch.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=1, groups=192)
        self.conv1_4 = torch.nn.Conv2d(in_channels=192, out_channels=192, kernel_size=1, groups=192)

    def forward(self, x1):
        x2 = self.conv1_1(x1)
        x3 = torch.tanh(x2)
        x4 = self.conv1_2(x3)
        x5 = torch.tanh(x4)
        x6 = self.conv1_3(x5)
        x7 = torch.tanh(x6)
        x8 = self.conv1_4(x7)
        x9 = torch.tanh(x8)
        return x9




func = ModelTanh().to('cuda')



x1 = torch.rand(1, 192, 28, 28)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpesexe1z4/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpesexe1z4', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpesexe1z4/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
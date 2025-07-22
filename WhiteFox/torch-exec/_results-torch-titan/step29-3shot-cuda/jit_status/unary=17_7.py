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
        super(Model, self).__init__()
        self.conv = torch.nn.ConvTranspose2d(12, 64, kernel_size=7, stride=(2, 1))
        self.conv1 = torch.nn.ConvTranspose2d(64, 256, kernel_size=7, stride=(2, 1))
        self.conv2 = torch.nn.ConvTranspose2d(256, 8, kernel_size=7, stride=(1, 1))

    def forward(self, x1):
        y_7 = self.conv(x1)
        y_8 = self.conv1(y_7)
        y_9 = self.conv2(y_8)
        return y_9




func = Model().to('cuda')



x1 = torch.randn(1, 12, 7, 7)


test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp_852k1z4/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp_852k1z4', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp_852k1z4/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
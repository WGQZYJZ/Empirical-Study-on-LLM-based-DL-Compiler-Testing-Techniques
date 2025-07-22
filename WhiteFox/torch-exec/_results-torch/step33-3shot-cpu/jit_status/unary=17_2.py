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
        self.conv1 = torch.nn.ConvTranspose2d(10, 64, kernel_size=4, stride=(2, 2), padding=(1, 1))
        self.conv2 = torch.nn.ConvTranspose2d(64, 128, kernel_size=4, stride=(2, 2), padding=(1, 1), dilation=(2, 2))
        self.conv3 = torch.nn.ConvTranspose2d(128, 64, kernel_size=4, stride=(2, 2), padding=(1, 1), dilation=(2, 2))
        self.conv4 = torch.nn.ConvTranspose2d(64, 16, kernel_size=4, stride=(2, 2), padding=(1, 1), dilation=(2, 2))
        self.conv5 = torch.nn.ConvTranspose2d(16, 3, kernel_size=4, stride=(2, 2), padding=(1, 1), dilation=(2, 2))

    def forward(self, x1):
        x = self.conv1(x1)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.conv5(x)
        return x



func = Model().to('cpu')


x1 = torch.randn(1, 10, 64, 64)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpia9kxxal/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpia9kxxal/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpia9kxxal', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
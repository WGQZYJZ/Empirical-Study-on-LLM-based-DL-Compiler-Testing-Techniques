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
        self.conv2d = torch.nn.Conv2d(3, 32, 7, 3)
        self.conv2d_1 = torch.nn.Conv2d(32, 48, 5, 1)
        self.conv2d_2 = torch.nn.ConvTranspose2d(48, 64, 2, 1)
        self.maxpool2d = torch.nn.MaxPool2d(kernel_size=3, stride=3, padding=1)
        self.avgpool2d = torch.nn.AvgPool2d(kernel_size=3, stride=2, padding=0)
        self.tanh = torch.nn.Tanh()
        self.softmax = torch.nn.Softmax()

    def forward(self, x):
        v1 = self.conv2d(x)
        v2 = self.conv2d_1(v1)
        v3 = self.conv2d_2(v2)
        v4 = self.maxpool2d(v3)
        v5 = self.avgpool2d(v4)
        x1 = self.tanh(v5)
        x2 = self.softmax(x1)
        return x2




func = ModelTanh().to('cuda')



x = torch.randn(64, 3, 112, 112)


test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp6qydo1tb/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmp6qydo1tb', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmp6qydo1tb/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
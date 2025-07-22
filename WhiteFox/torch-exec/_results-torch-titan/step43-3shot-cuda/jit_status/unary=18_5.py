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
        self.conv1 = torch.nn.Conv2d(in_channels=16, out_channels=160, kernel_size=1, stride=2, padding=2)
        self.conv2 = torch.nn.Conv2d(in_channels=160, out_channels=256, kernel_size=1, stride=1, padding=1, dilation=2)
        self.conv3 = torch.nn.Conv2d(in_channels=256, out_channels=320, kernel_size=1, stride=1, padding=0, dilation=5)
        self.conv4 = torch.nn.Conv2d(in_channels=320, out_channels=6400, kernel_size=(1, 3), stride=1, padding=(0, 2), dilation=4)
        self.conv5 = torch.nn.Conv2d(in_channels=6400, out_channels=160, kernel_size=1, stride=2, padding=3, dilation=6)
        self.conv6 = torch.nn.Conv2d(in_channels=160, out_channels=320, kernel_size=(1, 6), stride=1, padding=(2, 1), dilation=1)

    def forward(self, inp1):
        v1 = torch.sigmoid(self.conv1(inp1))
        v2 = torch.sigmoid(self.conv2(v1))
        v3 = torch.sigmoid(self.conv3(v2))
        v4 = torch.sigmoid(self.conv4(v3))
        v5 = torch.sigmoid(self.conv5(v4))
        v6 = torch.sigmoid(self.conv6(v5))
        return v6




func = Model().to('cuda')



inp1 = torch.randn(1, 16, 80, 80)


test_inputs = [inp1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpgyjbazff/main.c', '-O3', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/lib/python3.8/site-packages/triton/common/../third_party/cuda/include', '-I/home/yujunzhe/anaconda3/envs/titanfuzz/include/python3.8', '-I/tmp/tmpgyjbazff', '-shared', '-fPIC', '-lcuda', '-o', '/tmp/tmpgyjbazff/triton_.cpython-38-x86_64-linux-gnu.so', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-L/lib/i386-linux-gnu']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
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
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv3 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv4 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv5 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv6 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv7 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv8 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv9 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv10 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv11 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv12 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        v3 = self.conv3(x1)
        v4 = self.conv4(x1)
        v5 = v1 + v2 + v3 + v4 + self.conv5(x1) + self.conv6(x1) + self.conv7(x1) + self.conv8(x1)
        v6 = self.conv9(x1) + self.conv10(x1) + self.conv11(x1) + self.conv12(x1)
        v7 = v5 + v6
        v8 = torch.relu(v7)
        return v8



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp25932d2e/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp25932d2e/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp25932d2e', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
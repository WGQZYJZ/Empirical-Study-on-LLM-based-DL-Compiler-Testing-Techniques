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
        self.conv1_1 = torch.nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=12, bias=False)
        self.bn1_1 = torch.nn.BatchNorm2d(64)
        self.conv1_2 = torch.nn.Conv2d(64, 64, kernel_size=3, stride=1, padding=12, bias=False)
        self.bn1_2 = torch.nn.BatchNorm2d(64)
        pool1 = torch.nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        relu1 = torch.nn.ReLU(inplace=False)
        layers1 = torch.nn.Sequential(self.conv1_1, self.bn1_1, relu1, self.conv1_2, self.bn1_2, pool1)
        self.features1 = torch.nn.Sequential()
        self.features1.add_module('layers0', layers1)
        self.features1.add_module('ReLU1', torch.nn.ReLU(inplace=False))

    def forward(self, x):
        output = self.features1(x)
        return output



func = Model().to('cpu')


x1 = torch.randn(1, 3, 10, 10)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp35jkbvem/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp35jkbvem/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp35jkbvem', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
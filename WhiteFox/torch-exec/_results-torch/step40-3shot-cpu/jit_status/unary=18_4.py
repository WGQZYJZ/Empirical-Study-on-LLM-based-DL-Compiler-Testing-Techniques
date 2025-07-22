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
        self.layer1 = torch.nn.Sequential(torch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1), torch.nn.BatchNorm2d(num_features=16), torch.nn.ReLU(), torch.nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer2 = torch.nn.Sequential(torch.nn.Conv2d(in_channels=16, out_channels=32, kernel_size=5, stride=1, padding=2), torch.nn.BatchNorm2d(num_features=32), torch.nn.ReLU(), torch.nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer3 = torch.nn.Sequential(torch.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1), torch.nn.BatchNorm2d(num_features=64), torch.nn.ReLU(), torch.nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer4 = torch.nn.Sequential(torch.nn.Conv2d(in_channels=64, out_channels=1, kernel_size=3, stride=1, padding=1))

    def forward(self, x1):
        v1 = self.layer1.forward(x1)
        v2 = self.layer2.forward(v1)
        v3 = self.layer3.forward(v2)
        v4 = self.layer4.forward(v3)
        v5 = torch.sigmoid(v4)
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpkxe1n4bq/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpkxe1n4bq/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpkxe1n4bq', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
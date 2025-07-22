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
        torch.manual_seed(0)
        self.conv1 = torch.nn.Conv2d(1, 64, kernel_size=7, stride=4, padding=0, bias=False)
        self.bn1 = torch.nn.BatchNorm2d(64)
        self.relu1 = torch.nn.ReLU(inplace=False)
        self.pool1 = torch.nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        torch.manual_seed(0)
        self.conv2 = torch.nn.Conv2d(64, 128, kernel_size=1, stride=1, padding=0, bias=False)
        self.bn2 = torch.nn.BatchNorm2d(128)
        self.relu2 = torch.nn.ReLU(inplace=False)
        self.conv3 = torch.nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=0, bias=False)
        self.bn3 = torch.nn.BatchNorm2d(128)
        self.relu3 = torch.nn.ReLU(inplace=False)
        self.pool3 = torch.nn.MaxPool2d(kernel_size=3, stride=2, padding=1)

    def forward(self, x):
        t1 = self.pool1(self.relu2(self.bn2(self.conv2(self.relu1(self.bn1(self.conv1(x)))))))
        t2 = self.relu3(self.bn3(self.conv3(t1)))
        return self.pool3(t2)



func = Model().to('cpu')


x1 = torch.randn(4, 1, 224, 224)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpcu_3tm5n/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpcu_3tm5n/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpcu_3tm5n', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
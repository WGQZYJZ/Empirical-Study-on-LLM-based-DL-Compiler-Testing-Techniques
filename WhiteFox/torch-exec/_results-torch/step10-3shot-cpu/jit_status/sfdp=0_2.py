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
        self.layer1 = torch.nn.Sequential(torch.nn.Sequential(torch.nn.BatchNorm2d(3, eps=1e-08, momentum=0.1, affine=True, track_running_stats=True), torch.nn.Conv2d(3, 74, (1, 1), stride=(1, 1), bias=False)), torch.nn.Sequential(torch.nn.BatchNorm2d(74, eps=1e-08, momentum=0.1, affine=True, track_running_stats=True), torch.nn.Conv2d(74, 74, (3, 3), stride=(1, 1), padding=(1, 1), bias=False)))
        self.layer2 = torch.nn.Sequential(torch.nn.Sequential(torch.nn.BatchNorm2d(74, eps=1e-08, momentum=0.1, affine=True, track_running_stats=True), torch.nn.Conv2d(74, 74, (1, 1), stride=(1, 1), bias=False)), torch.nn.Sequential(torch.nn.BatchNorm2d(74, eps=1e-08, momentum=0.1, affine=True, track_running_stats=True), torch.nn.Conv2d(74, 1, (3, 3), stride=(1, 1), padding=(1, 1), bias=False)))

    def forward(self, x1):
        x = self.layer1(x1)
        x = self.layer2(x).squeeze()
        return x



func = Model().to('cpu')


x1 = torch.randn(5, 3, 224, 224)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpxs6xztxj/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpxs6xztxj/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpxs6xztxj', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
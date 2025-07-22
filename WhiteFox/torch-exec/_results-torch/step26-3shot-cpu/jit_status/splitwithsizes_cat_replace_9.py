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
        self.conv2d = torch.nn.Sequential(torch.nn.AdaptiveAvgPool2d(7), torch.nn.AlphaDropout(0.0), torch.nn.Conv2d(3, 3, 1, 1, 0), torch.nn.ReLU6(), torch.nn.AdaptiveMaxPool2d(7), torch.nn.AdaptiveAvgPool2d((2, 2)), torch.nn.Conv2d(3, 3, 1, 1, 0), torch.nn.ReLU())
        self.relu = torch.nn.Sequential(torch.nn.AdaptiveAvgPool2d((2, 2)), torch.nn.Conv2d(3, 3, 1, 1, 0), torch.nn.ReLU(), torch.nn.Sigmoid(), torch.nn.ReLU(), torch.nn.BatchNorm2d(1), torch.nn.Conv2d(1, 1, 1, 1, 0), torch.nn.ReLU())
        self.conv2d1 = torch.nn.Sequential(torch.nn.Conv2d(3, 3, 1, 1, 0), torch.nn.Sigmoid(), torch.nn.BatchNorm2d(3), torch.nn.ReLU(), torch.nn.ReLU(), torch.nn.Softmax(dim=1))
        self.pad = torch.nn.Sequential(torch.nn.ConstantPad3d(1, value=3.964261))

    def forward(self, v1):
        split_tensors = torch.split(v1, [1, 1], dim=0)
        concatenated_tensor = torch.cat(split_tensors, dim=0)
        return (concatenated_tensor, torch.split(v1, [1, 2], dim=1))



func = Model().to('cpu')


x = torch.randn(2, 3, 64, 64)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp6og80y3m/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp6og80y3m/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp6og80y3m', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
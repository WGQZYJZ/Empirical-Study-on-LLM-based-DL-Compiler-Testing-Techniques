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
        self.features0 = torch.nn.Conv2d(3, 32, 3, 2, 2, bias=False)
        self.features1 = torch.nn.Conv2d(32, 32, 3, 1, 1, bias=False)
        self.activation1 = torch.nn.ReLU()
        self.features2 = torch.nn.Conv2d(32, 32, 3, 1, 1, bias=False)
        self.activation2 = torch.nn.ReLU()
        self.join_tensor = torch.nn.Sequential()
        self.features7 = torch.nn.Conv2d(32, 32, 3, 2, 2, bias=False)
        self.features8 = torch.nn.Conv2d(32, 32, 3, 1, 1, bias=False)
        self.activation3 = torch.nn.ReLU()
        self.features9 = torch.nn.Conv2d(32, 32, 3, 1, 1, bias=False)
        self.activation4 = torch.nn.ReLU()

    def forward(self, x):
        split_tensors = torch.split(x, [1, 1, 1], dim=1)
        concatenated_tensor = torch.cat(split_tensors, dim=1)
        return (concatenated_tensor, torch.split(x, [1, 1, 1], dim=1))



func = Model().to('cuda')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmph4fp974e/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmph4fp974e/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmph4fp974e', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
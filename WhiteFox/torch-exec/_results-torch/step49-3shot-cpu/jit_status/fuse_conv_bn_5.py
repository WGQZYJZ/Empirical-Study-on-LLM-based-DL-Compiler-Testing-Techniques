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
        self.fc_1 = torch.nn.Linear(16, 16)
        self.bn1 = torch.nn.BatchNorm1d(16)
        self.relu_1 = torch.nn.ReLU()
        self.fc_2 = torch.nn.Linear(16, 16)
        self.bn2 = torch.nn.BatchNorm1d(16)
        self.relu_2 = torch.nn.ReLU()
        self.fc_3 = torch.nn.Linear(16, 10)

    def forward(self, x):
        x = self.fc_1(x)
        x = self.bn1(x)
        x = self.relu_1(x)
        x = self.fc_2(x)
        x = self.bn2(x)
        x = self.relu_2(x)
        x = self.fc_3(x)
        return x



func = Model().to('cpu')


x = torch.randn(16, 16)

test_inputs = [x]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpl8g3350s/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpl8g3350s/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpl8g3350s', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
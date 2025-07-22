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
        self.conv1 = torch.nn.Conv1d(7, 7, 3)
        self.conv2 = torch.nn.Conv1d(7, 8, 3)
        torch.manual_seed(1)
        self.bn1 = torch.nn.BatchNorm1d(7)
        torch.manual_seed(0)
        self.bn2 = torch.nn.BatchNorm1d(8)
        torch.manual_seed(1)
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        t1 = self.relu(self.bn1(self.conv1(x1)))
        t2 = self.relu(self.bn2(self.conv2(t1)))
        y = torch.tanh(t2)
        return (t1, t2, y)



func = Model().to('cpu')


x1 = torch.randn(1, 7, 6)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmp91l048ue/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmp91l048ue/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmp91l048ue', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''
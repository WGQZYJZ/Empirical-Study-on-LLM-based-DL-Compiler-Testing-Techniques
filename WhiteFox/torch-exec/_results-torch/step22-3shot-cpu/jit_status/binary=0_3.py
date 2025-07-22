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
        self.layers = [['conv', torch.nn.Conv2d(3, 8, 1, stride=1, padding=1), 1]]

    def forward(self, x1, other=1, padding1=None):
        for k in range(len(self.layers)):
            [op_name, op, stride] = self.layers[k]
            if op_name == 'pool':
                x1 = F.avg_pool2d(x1, op.kernel_size, stride=op.stride, padding=op.padding)
            elif op_name == 'conv':
                x1 = op(x1)
            elif op_name == 'bn':
                x1 = op(x1, self.training)
            elif op_name == 'relu':
                x1 = F.relu(x1)
            elif op_name == 'fc':
                x1 = F.linear(x1.flatten(1), op.weight, op.bias)
            elif op_name == 'add':
                x1 = x1 + op
            if padding1 == None:
                padding1 = torch.randn(x1.shape)
            x1 = x1 + other
        return x1



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_STATUS
'''
direct:


jit:
backend='inductor' raised:
CalledProcessError: Command '['/usr/local/bin/gcc', '/tmp/tmpfhv5cr3x/main.c', '-O3', '-shared', '-fPIC', '-Wno-psabi', '-o', '/tmp/tmpfhv5cr3x/cuda_utils.cpython-39-x86_64-linux-gnu.so', '-lcuda', '-L/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/lib', '-L/lib/x86_64-linux-gnu', '-L/lib/i386-linux-gnu', '-I/home/yujunzhe/anaconda3/envs/whitefox/lib/python3.9/site-packages/triton/backends/nvidia/include', '-I/tmp/tmpfhv5cr3x', '-I/home/yujunzhe/anaconda3/envs/whitefox/include/python3.9']' returned non-zero exit status 1.


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''